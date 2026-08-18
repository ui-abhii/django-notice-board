# 🚀 Dockerized Django Notice Board

A Dockerized **Django Notice Board** application demonstrating containerization of a Python web application using Docker. This project showcases fundamental DevOps practices such as Docker image creation, container management, dependency management, and version control with Git & GitHub.

---

## 📌 Project Overview

The project has been containerized using Docker and configured to use PostgreSQL as the database.

Docker Compose is used to run the Django application and PostgreSQL database as separate services, with container networking, healthchecks, service dependencies, and persistent database storage.

---

## ✨ Features

- 📝 Notice Board web application
- 🐍 Built with Django
- 🐳 Dockerized using a custom Dockerfile
- 🐘 PostgreSQL database integration
- 📦 Dependency management with requirements.txt
- 🔐 Django Admin Panel
- 🔑 Environment-based database configuration
- 💻 Cross-platform deployment using Docker
- - 🧩 Docker Compose multi-container setup
- 🔗 Container networking between Django and PostgreSQL
- ❤️ PostgreSQL healthcheck
- 💾 Persistent PostgreSQL volume

---

## 🛠️ Tech Stack

| **Technology** | **Purpose** |
|----------------|-------------|
| Python         | Programming Language |
| Django         | Web Framework |
| PostgreSQL     | Relational Database |
| Docker         | Containerization |
| Docker Compose | Multi-container orchestration |
| Git            | Version Control |
| GitHub         | Code Hosting |

---
## 📂 Project Structure

```text
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
---

## ⚙️ Prerequisites

- Docker Desktop
- Git

> PostgreSQL does not need to be installed separately because it runs in a Docker container.
---

## 🐘 PostgreSQL Configuration

The application uses PostgreSQL as its database.

Create a `.env` file based on the provided `.env.example` file and configure your PostgreSQL database credentials.

Example:

```env
DB_NAME=noticeboard
DB_USER=noticeboard
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

## 🐳 Run with Docker Compose

Build and start the Django and PostgreSQL services:

```bash
docker compose up --build

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
- Configure Django to use PostgreSQL
- Manage database configuration using environment variables
- Use Git and GitHub for version control
- Configure Docker Desktop with WSL 2
- Add Docker Compose support

---

## 🚀 Future Improvements

- [ ] Deploy on AWS EC2
- [ ] Configure Nginx and Gunicorn
- [ ] Add CI/CD pipeline using GitHub Actions
- [ ] Add automated testing


---


