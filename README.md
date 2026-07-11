# 🚀 Dockerized Django Notice Board

A Dockerized **Django Notice Board** application demonstrating containerization of a Python web application using Docker. This project showcases fundamental DevOps practices such as Docker image creation, container management, dependency management, and version control with Git & GitHub.

---

## 📌 Project Overview

This application allows users to manage notices through a Django web interface. The project has been containerized using Docker, enabling consistent deployment across different environments.

---

## ✨ Features

- 📝 Notice Board web application
- 🐍 Built with Django
- 🐳 Dockerized using a custom Dockerfile
- 📦 Dependency management with `requirements.txt`
- 🔐 Django Admin Panel
- 💻 Cross-platform deployment using Docker

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Django | Web Framework |
| Docker | Containerization |
| SQLite | Database |
| Git | Version Control |
| GitHub | Code Hosting |

---

## 📂 Project Structure

```text
notice-board-app/
│
├── demo/                  # Django application
├── devops/                # Django project configuration
├── Dockerfile             # Docker image configuration
├── .dockerignore
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Prerequisites

Before running the project, ensure you have:

- Docker Desktop
- Git

---

## 📥 Clone the Repository

```bash
git clone https://github.com/ui-abhii/dockerized-django-notice-board.git
cd dockerized-django-notice-board
```

*(Replace the repository URL if you use a different name.)*

---

## 🐳 Build the Docker Image

```bash
docker build -t notice-board-app .
```

---

## ▶️ Run the Docker Container

```bash
docker run -d -p 8000:8000 --name notice-board notice-board-app
```

---

## 🌐 Access the Application

Open your browser:

**Application**

```
http://localhost:8000/demo/
```

**Admin Panel**

```
http://localhost:8000/admin/
```

---

## 🛑 Stop the Container

```bash
docker stop notice-board
```

---

## 🗑️ Remove the Container

```bash
docker rm notice-board
```

---

## 📸 Screenshots

> Add screenshots after pushing the project.

### Home Page

```
screenshots/home.png
```

### Admin Dashboard

```
screenshots/admin.png
```

---

## 📚 Docker Commands Used

```bash
# Build image
docker build -t notice-board-app .

# Run container
docker run -d -p 8000:8000 --name notice-board notice-board-app

# View running containers
docker ps

# Stop container
docker stop notice-board

# Remove container
docker rm notice-board

# View Docker images
docker images
```

---

## 🎯 Learning Outcomes

Through this project, I learned how to:

- Containerize a Django application using Docker
- Create and use a Dockerfile
- Build and run Docker images
- Expose application ports
- Manage Python dependencies inside containers
- Use Git and GitHub for version control
- Configure Docker Desktop with WSL 2

---

## 🚀 Future Improvements

- [ ] Add Docker Compose support
- [ ] Use PostgreSQL instead of SQLite
- [ ] Deploy on AWS EC2
- [ ] Configure Nginx and Gunicorn
- [ ] Add CI/CD pipeline using GitHub Actions
- [ ] Add automated testing


---

⭐ If you found this project useful, consider giving it a star!
