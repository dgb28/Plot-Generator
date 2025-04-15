# 🚀 Plot Generator Backend
🎨 Write Python or R code and generate beautiful visualizations in real-time. Built with React + Vite, Django, and Docker.

## 🌟 Overview  
This is the backend interface for **Plot generator**, a platform that lets users write Python or R code to generate beautiful visualizations — all executed in secure Docker containers on the backend. Users can write code, run it, and view visual or HTML outputs right in the browser.

## 🧠 Key Features  
- 📝 Interactive code editor with syntax highlighting (Ace Editor)  
- 🐳 Secure backend code execution using custom Docker containers  
- 📦 Supports Python & R with popular libraries:  
  `matplotlib`, `numpy`, `pandas`, `seaborn`, `scikit-learn`, `plotly`, `lattice`, `rgl`, `fs`, `htmlwidgets`  
- 🖼️ Outputs include:  
  - Standard output & error logs  
  - Base64-encoded images  
  - Interactive Plotly charts rendered via `<iframe>`  
- 🔌 Seamless backend integration using REST API  
- 🌗 Dark theme UI with TailwindCSS  
- 🚀 Built with React (Vite) + Django REST Framework  
- ⚡ Optimized for speed and lightweight performance with Vite

## 🧩 Tech Stack  
### Frontend
- React + Vite  
- TailwindCSS  
- Ace Editor  
- REST integration with backend
- 👉 [CodePlotter Frontend (Django)](https://github.com/dgb28/Plot-Generator-ui)

### Backend
- Django + Django REST Framework  
- Docker SDK for Python  
- Local media storage for `.html` plots  
- Custom Docker images for executing Python and R scripts

---

## 🎬 Demo Video Link
https://youtu.be/mEBfLgDtqrs

---
## 🐞 Issues Encountered & Resolutions

- **Issue:** Backend containers couldn’t access required Python or R libraries  
  **Resolution:** Created custom Docker images with all required libraries pre-installed and pushed to Docker Hub.

- **Issue:** Cross-Origin Resource Sharing (CORS) errors between frontend and backend  
  **Resolution:** Configured CORS headers in Django to allow frontend access.

- **Issue:** HTML plot rendering wasn’t loading in frontend  
  **Resolution:** Used Django's `media` folder to serve `.html` files and rendered them using `<iframe>` in the frontend.
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
# Start Django server
python manage.py runserver  # Runs at http://127.0.0.1:8000
```
## 🧪 Sample Code Snippets
🐍 Python Scripts
1. Static Plot with Matplotlib + Seaborn + Scikit-learn + Pandas
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame
df['target'] = iris.target

sns.pairplot(df, hue='target', palette='Set1')
plt.suptitle("Static Pairplot of Iris Dataset", y=1.02)
plt.tight_layout()
plt.savefig("static_plot.png")
plt.show()

```
2. Interactive Plot with Plotly + Pandas + Scikit-learn
```python
import pandas as pd
import plotly.express as px
from sklearn.datasets import load_wine

df = load_wine(as_frame=True).frame
df['target'] = load_wine().target

fig = px.scatter(
    df,
    x='alcohol',
    y='malic_acid',
    color='target',
    hover_data=['ash', 'alcalinity_of_ash'],
    title="Interactive Scatter Plot of Wine Dataset"
)

fig.write_html("interactive_plot.html")
fig.show()

```
3. 3D Interactive Plot with Plotly
```python
import pandas as pd
import plotly.express as px
from sklearn.datasets import load_breast_cancer

df = load_breast_cancer(as_frame=True).frame
df['target'] = load_breast_cancer().target

fig = px.scatter_3d(
    df,
    x='mean radius',
    y='mean texture',
    z='mean perimeter',
    color='target',
    title="3D Interactive Plot - Breast Cancer Dataset"
)

fig.write_html("3d_interactive_plot.html")
fig.show()

```
📊 R Scripts
1. 3D Interactive Plot with rgl + htmlwidgets
```R
library(rgl)
library(htmlwidgets)

x <- rnorm(100)
y <- rnorm(100)
z <- rnorm(100)

open3d(useNULL = TRUE)
plot3d(x, y, z, col = rainbow(100), size = 5)

htmlwidgets::saveWidget(rglwidget(), "rgl_plot.html", selfcontained = TRUE)
```
2. Lattice Plot
```R
library(lattice)

data(mtcars)

png("lattice_plot.png")
splom(~mtcars[1:4], data = mtcars, main = "MTCARS Scatterplot Matrix")
dev.off()

```
---

## 👥 Collaborators  
| Name           | Email              |
|----------------|--------------------|
| Dhruv Bhanderi | dbhander@iu.edu    |
|                | dgbhanderi20@gmail.com |

---

## 💡 Notes
- Docker must be installed and running locally  
- Backend and frontend run independently and communicate over `http://localhost`  
- Generated `.html` files are stored in `backend/media/`  
- You can serve those files using Django’s static/media config locally

---

## 🏁 You're all set!
Now go to `http://localhost:5173` and start generating visualizations 🚀
