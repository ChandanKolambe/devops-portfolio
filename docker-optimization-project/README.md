# 🐳 Docker Optimization Project - Production-Grade Containerization

[![Docker Build & Security Scan](https://github.com/ChandanKolambe/devops-portfolio/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/ChandanKolambe/devops-portfolio/actions/workflows/ci.yaml)
[![Docker Image Size](https://img.shields.io/docker/image-size/chandankolambe/optimized-flask/latest?label=Optimized%20Image%20Size)](https://hub.docker.com/r/chandankolambe/optimized-flask)

Demonstrates **industry best practices** for Docker optimization, security, and CI/CD automation.  
**Key Achievements:** 85% size reduction • Zero-downtime deployments   

## 📊 Optimization Results (Before vs After)
| Metric               | Before       | After       | Reduction |
|----------------------|-------------|-------------|-----------|
| **Image Size**       | 1.15 GB     | 189 MB      | 85% ↓     |

![Size Comparison]()

---

## 🛠️ Technical Implementation

### 🔧 Key Optimizations
1. **Multi-stage Builds**  
   - Builder stage: Installs build dependencies  
   - Final stage: Only keeps runtime essentials  
   ```dockerfile
   FROM python:3.8-slim as builder
   # ... build steps ...
   FROM python:3.8-slim
   COPY --from=builder /opt/venv /opt/venv

## 🚀 Quick Start
### Local Development
```bash
# 1. Clone repo
git clone https://github.com/ChandanKolambe/devops-portfolio.git
cd devops-portfolio/docker-optimization-project

# 2. Start with compose
docker-compose up -d

# Access app at http://localhost:5000
```

### Production Deployment
```bash
# Build optimized image
docker build -t chandankolambe/optimized-flask .

# Run with security flags
docker run -d \
  --name myapp \
  -p 5000:5000 \
  --read-only \
  --security-opt no-new-privileges \
  chandankolambe/optimized-flask
```
