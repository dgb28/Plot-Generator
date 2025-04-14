import os
import tempfile
import docker
import base64
from rest_framework.decorators import api_view
from rest_framework.response import Response
from docker.errors import ContainerError
from django.conf import settings
import re

def get_docker_image_and_ext(language):
    if language == "python":
        return "dgbhanderi/python-executor", ".py"
    elif language == "r":
        return "dgbhanderi/r-executor", ".R"
    else:
        raise ValueError("Unsupported language")

def encode_images_from_dir(directory):
    encoded_images = []
    for file in os.listdir(directory):
        if file.endswith(".png"):
            with open(os.path.join(directory, file), "rb") as img:
                encoded_images.append(base64.b64encode(img.read()).decode("utf-8"))
    return encoded_images

def save_and_get_html_url(file_path, filename, request):
    os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
    dest_path = os.path.join(settings.MEDIA_ROOT, filename)
    with open(file_path, "r", encoding="utf-8") as src, open(dest_path, "w", encoding="utf-8") as dest:
        dest.write(src.read())
    return request.build_absolute_uri(settings.MEDIA_URL + filename)

def patch_plotly_for_html(code):
    if "plotly" in code.lower() and ".show()" in code:
        match = re.search(r"(\w+)\.show\s*\(\s*\)", code)
        if match:
            fig_var = match.group(1)
            code = code.replace(match.group(0), f'{fig_var}.write_html("plot.html")')
    return code

@api_view(["POST"])
def run_code(request):
    code = request.data.get("code")
    language = request.data.get("language")

    if not code or not language:
        return Response({"stderr": "Missing code or language."}, status=400)

    try:
        image, extension = get_docker_image_and_ext(language)
    except ValueError as e:
        return Response({"stderr": str(e), "stdout": "", "images": [], "html_url": None}, status=400)

    if language == "python":
        code = patch_plotly_for_html(code)

    with tempfile.TemporaryDirectory() as tmpdir:
        filename = f"snippet{extension}"
        filepath = os.path.join(tmpdir, filename)

        with open(filepath, "w") as f:
            f.write(code)

        try:
            client = docker.from_env()
            command = ["python", f"/code/{filename}"] if language == "python" else ["Rscript", f"/code/{filename}"]

            container_output = client.containers.run(
                image=image,
                command=command,
                volumes={tmpdir: {"bind": "/code", "mode": "rw"}},
                working_dir="/code",
                stderr=True,
                stdout=True,
                remove=True,
            )

            output_text = container_output.decode("utf-8") if isinstance(container_output, bytes) else str(container_output)
            images = encode_images_from_dir(tmpdir)

            html_url = None
            for file in os.listdir(tmpdir):
                if file.endswith(".html"):
                    html_url = save_and_get_html_url(os.path.join(tmpdir, file), file, request)
                    break

            return Response({
                "stdout": output_text,
                "stderr": "",
                "images": images,
                "html_url": html_url
            })

        except ContainerError as e:
            err = e.stderr
            error_text = err.decode("utf-8") if isinstance(err, bytes) else str(e)
            return Response({
                "stdout": "",
                "stderr": error_text,
                "images": [],
                "html_url": None
            }, status=500)
        except Exception as e:
            return Response({
                "stdout": "",
                "stderr": str(e),
                "images": [],
                "html_url": None
            }, status=500)
