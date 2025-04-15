#🚀 Plot Generator Backend  
🔬 A secure Docker-powered code execution engine built with Django

##🌟 Overview  
This is the backend for **Plot Generator**, where submitted Python and R code is executed inside containerized environments using your custom Docker images. The output (including images or interactive Plotly HTML files) is returned via REST API.

##🔒 Secure Execution  
- 🐳 Executes user code in Docker containers  
- 📦 Custom Docker images: `python-executor` and `r-executor`  
- 🖼️ Encodes image output as base64  
- 🌐 Generates and stores interactive Plotly charts as `.html` files  

##🧠 Core Components  
- Django + Django REST Framework  
- Docker SDK for Python  
- Local storage for Html & Plots (Use persistant storage or database for production deployment)
- CORS-enabled API for frontend use  

## 🔗 Frontend Repository  
👉 [CodePlotter Backend (Django)](https://github.com/dgb28/Plot-Generator-ui)

📦 How to Run Locally  
```bash
# Clone the repo
git clone https://github.com/your-username/codeplotter-backend.git
cd Plot-Generator

# Set up virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver
# Install dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver
