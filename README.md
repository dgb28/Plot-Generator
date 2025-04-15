# 🚀 CodePlotter  
🎨 Write Python or R code and generate beautiful visualizations in real-time. Built with React, Django, and Docker.

## 🌟 Overview  
**Plot Generator** is a full-stack application that lets users write Python or R code, execute it securely in Docker containers, and visualize the output instantly — including console output, images, and interactive Plotly HTML charts.

## 🧠 Key Features  
- 📝 Interactive code editor with Ace Editor  
- 🐳 Secure backend code execution using custom Docker containers  
- 📦 Python & R support with `matplotlib`, `numpy`, `pandas`, `seaborn`, `scikit-learn`, `plotly`, `lattice`, `rgl`, `fs`, `htmlwidgets`  
- 🖼️ Outputs include standard output, error logs, base64-encoded images, and Plotly HTML  
- 🌐 Built with React (Vite) frontend + Django REST backend

## 🧩 Tech Stack  
### Frontend
- React + Vite  
- TailwindCSS  
- Ace Editor  
- REST integration with backend

### Backend
- Django + Django REST Framework  
- Docker SDK for Python  
- Local media storage for `.html` plots  
- Custom Docker images for executing Python and R scripts

---

## 📂 Project Structure

```
CodePlotter/
├── frontend/        # React + Vite UI
├── backend/         # Django REST API
│   └── media/       # Stores HTML plots
│   └── code_executors/
│       ├── python/  # Dockerfile + snippet.py
│       └── r/       # Dockerfile + snippet.R
```

---

## 🛠️ How to Run the Entire App Locally

### 1️⃣ Clone the Repository
```bash
https://github.com/dgb28/Plot-Generator.git
cd Plot-Generator
```

---

### 2️⃣ Set Up the Backend (Django)

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
## 🐳 Build and Push Docker Executor Images

The backend uses two Docker images to securely execute code. You **must build and push** them to your Docker Hub account before running the app.

### 🔧 Python Executor
```bash
cd backend/myproject/code_executors/python

# Build image
docker build -t your-dockerhub-username/python-executor .

# Push to Docker Hub
docker push your-dockerhub-username/python-executor
```

### 🔧 R Executor
```bash
cd ../r

# Build image
docker build -t your-dockerhub-username/r-executor .

# Push to Docker Hub
docker push your-dockerhub-username/r-executor
```

### ✅ Update backend image names in `views.py`:
```python
def get_docker_image_and_ext(language):
    if language == "python":
        return "your-dockerhub-username/python-executor", ".py"
    elif language == "r":
        return "your-dockerhub-username/r-executor", ".R"
```
```bash
# Run migrations
python manage.py migrate

# Start Django server
python manage.py runserver  # Runs at http://127.0.0.1:8000
```

## 📦 API Reference

### `POST /api/execute/`

**Request Body:**
```json
{
  "code": "your Python or R code",
  "language": "python" | "r"
}
```

**Response:**
```json
{
  "stdout": "Console output",
  "stderr": "Errors if any",
  "images": ["base64-string", "..."],
  "html_url": "http://127.0.0.1:8000/media/plot.html"
}
```

---

## 👥 Collaborators  
| Name           | Email              |
|----------------|--------------------|
| Dhruv Bhanderi | dbhander@iu.edu    |

---

## 💡 Notes
- Docker must be installed and running locally  
- Backend and frontend run independently and communicate over `http://localhost`  
- Generated `.html` files are stored in `backend/media/`  
- You can serve those files using Django’s static/media config locally

---

## 🏁 You're all set!
Now go to `http://localhost:5173` and start generating visualizations 🚀
