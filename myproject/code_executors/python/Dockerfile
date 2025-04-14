#FROM python:3.10-slim
#
#WORKDIR /code
#COPY snippet.py /code/snippet.py

FROM python:3.10-slim

# Avoid interactive prompts during install
ENV DEBIAN_FRONTEND=noninteractive

# Install pip packages
RUN pip install --no-cache-dir matplotlib numpy pandas seaborn scikit-learn plotly

# Set working directory
WORKDIR /code
COPY snippet.py /code/snippet.py
# Set default command (overridden when running with different scripts)
CMD ["python", "/code/snippet.py"]