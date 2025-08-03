# 🐳 Docker Projects

This repo contains two main Docker-based projects:

1. **Challenge** — Multi-container Flask + Redis application with Nginx reverse proxy and load balancing.
2. **hello_flask** — Flask + MySQL application containerized with Docker.

---

## 📂 1. Challenge — Flask + Redis + Nginx

### **Overview**
A simple Python Flask web app connected to a Redis database.  
Nginx is used as a reverse proxy to load balance multiple Flask instances.

### **Features**
- **Flask** — Python web framework for serving pages.
- **Redis** — Key-value store to track visit counts.
- **Nginx** — Reverse proxy and load balancer.
- **Docker Compose** — Multi-container orchestration.

---

### **Endpoints**
- `/` → Welcome page with button to `/count`.
- `/count` → Increments and displays visit count (shared across all instances via Redis).

---

### **How to Run**
1. Build and start services:
  
   ```bash
   docker compose up --build
   ```
2. Scale Flask app to multiple instances:
    ```bash
    docker compose up --scale web=3 --build
    ```
3. Visit:
    - Home page: http://localhost:5002
    - Count page: http://localhost:5002/count

### **Persistent Redis Storage**
Redis data is stored in a Docker volume (redis-data) so the count persists between container restarts.

### **Nginx Reverse Proxy**

### **The nginx.conf file configures Nginx to:**

 - Listen on port 5002
 - Load balance requests between web containers

## 📂 2. hello_flask — Flask + MySQL

### **Overview**
A Python Flask application connected to a MySQL database using Docker Compose.

### **How to Run**

Build and start:

```bash
docker compose up --build
```
Visit the app:

```bash
http://localhost:5002
```

### **MySQL Configuration**

- MySQL root password: my-secret-pw (set in docker-compose.yml)
- Database service name: mydb (used as DB_HOST in Flask app)
- Persistent storage via Docker volume for MySQL data

## Notes

- The Challenge project demonstrates multi-container architecture and load balancing.
- The hello_flask project demonstrates Dockerizing a database-backed web app.
- Both projects can be adapted for AWS ECR deployment.