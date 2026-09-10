# System Health & Observability Dashboard API

A Flask-based SRE/DevOps mini-project that provides application, service, database, and system health information.

The project demonstrates an end-to-end workflow using **Git, GitHub, Pytest, Docker, and Jenkins**.

---

## 🚀 Features

- Application health monitoring
- Application version and environment configuration
- Service status monitoring
- SQLite database health check
- CPU and memory monitoring
- Application uptime and timestamp
- Automated API testing with Pytest
- Docker containerization
- Jenkins CI pipeline
- Docker image tagging using Jenkins build numbers
- Runtime health verification

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Application |
| Flask | REST API |
| Pytest | Automated testing |
| SQLite | Database |
| psutil | System metrics |
| Git/GitHub | Version control |
| Docker | Containerization |
| Jenkins | CI automation |

---

## 📁 Project Structure

```text
service-health-dashboard/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── tests/
│       └── test_app.py
│
├── database/
│   └── database.py
│
├── Dockerfile
├── .dockerignore
├── .gitignore
├── jenkins.Dockerfile
├── Jenkinsfile
└── README.md
```

---

## 🌐 API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/health` | Application liveness |
| GET | `/version` | Application version |
| GET | `/environment` | Runtime environment |
| GET | `/services` | Available services |
| GET | `/services/status` | Service health status |
| GET | `/database/health` | Database health |
| GET | `/database/info` | Database information |
| GET | `/system/summary` | Overall system summary |

### Example

```text
GET /health
```

Example response:

```json
{
  "status": "UP"
}
```

---

## ⚙️ Local Setup

### 1. Clone Repository

```powershell
git clone https://github.com/Ashmita-2026/Mini-Project-.git
cd Mini-Project-
```

### 2. Create Virtual Environment

```powershell
python -m venv venv
```

### 3. Activate Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```powershell
pip install -r app/requirements.txt
```

---

## ▶️ Run the Application

Start the Flask application:

```powershell
python app/app.py
```

The application runs on:

```text
http://localhost:5000
```

### Test the API

```powershell
curl http://localhost:5000/health
curl http://localhost:5000/version
curl http://localhost:5000/environment
curl http://localhost:5000/services
curl http://localhost:5000/database/health
curl http://localhost:5000/database/info
curl http://localhost:5000/services/status
curl http://localhost:5000/system/summary
```

---

## 🧪 Testing

Run all automated tests with:

```powershell
pytest app/tests
```

Expected result:

```text
8 passed
```

The test suite covers all eight API endpoints using Flask's test client.

---

## 🐳 Docker

### Build Docker Image

```powershell
docker build -t service-health-dashboard:1.1.0 .
```

### Run Docker Container

```powershell
docker run --rm -p 5000:5000 -e APP_ENV=development -e APP_VERSION=1.1.0 service-health-dashboard:1.1.0
```

### Test Containerized API

```powershell
curl http://localhost:5000/health
curl http://localhost:5000/version
curl http://localhost:5000/environment
curl http://localhost:5000/services
curl http://localhost:5000/database/health
curl http://localhost:5000/database/info
curl http://localhost:5000/services/status
curl http://localhost:5000/system/summary
```

### Environment Configuration

The application uses environment variables instead of hardcoding runtime configuration.

```text
APP_ENV
APP_VERSION
```

Example:

```text
APP_ENV=development
APP_VERSION=1.1.0
```

---

## 🔄 Git Workflow

The project follows a feature-branch workflow using `main`, `develop`, and feature branches.

```text
main
  │
  └── develop
       │
       ├── feature/add-version
       ├── feature/add-services
       ├── feature/update-health
       └── feature/change-health-status
```

### Feature Branches

- `feature/add-version` — added `/version` and `/environment`
- `feature/add-services` — added `/services`
- `feature/update-health` — changed the health response
- `feature/change-health-status` — created a second change to the same health response

### Merge Conflict

A controlled merge conflict was intentionally created between the two health-related branches.

The conflict was manually resolved by choosing the required implementation, removing Git conflict markers, committing the resolution, and rerunning the tests.

The Git workflow was:

```text
Feature Branch
      ↓
   develop
      ↓
     main
```

The project uses small, logical commits to maintain a clear and understandable Git history.

---

## 🔧 Jenkins CI Pipeline

Jenkins automates application validation and Docker verification.

### Pipeline Flow

```text
Checkout
   ↓
Install
   ↓
Test
   ↓
Build
   ↓
Tag
   ↓
Health Check
```

### 1. Checkout

Jenkins checks out the project from GitHub using the `develop` branch.

### 2. Install

Jenkins creates an isolated Python virtual environment:

```text
.jenkins-venv
```

Dependencies are installed from:

```text
app/requirements.txt
```

### 3. Test

Jenkins runs:

```bash
.jenkins-venv/bin/pytest app/tests
```

All eight automated tests must pass before the pipeline continues.

### 4. Build

Jenkins builds the Docker image:

```text
service-health-dashboard:latest
```

### 5. Tag

The image is tagged using the Jenkins build number:

```text
service-health-dashboard:<BUILD_NUMBER>
```

Example:

```text
service-health-dashboard:9
```

### 6. Health Check

Jenkins starts a temporary container using the tagged Docker image and verifies:

```text
/health
/database/health
/services/status
/system/summary
```

After verification, the temporary container is removed.

This ensures that the Docker image built by Jenkins can successfully start and respond to health requests.

---

## 🏥 Health Model

The application provides different levels of health information.

### Application Health

Endpoint:

```text
/health
```

Example response:

```json
{
  "status": "UP"
}
```

This is a lightweight application liveness check.

### Database Health

Endpoint:

```text
/database/health
```

The application performs a real SQLite database connection and executes:

```sql
SELECT 1;
```

If the operation succeeds:

```text
Database → UP
```

If the database operation fails:

```text
Database → DOWN
```

### Service Status

Endpoint:

```text
/services/status
```

Reports the status of the API and database services.

Example:

```json
{
  "services": [
    {
      "name": "API",
      "status": "UP"
    },
    {
      "name": "Database",
      "status": "UP"
    }
  ],
  "total_services": 2
}
```

### System Summary

Endpoint:

```text
/system/summary
```

Provides:

- Overall health status
- Environment
- Application version
- Database status
- Service count
- CPU usage
- Memory usage
- Application uptime
- Current timestamp

Overall status is calculated from database health:

```text
Database UP
     ↓
Overall UP
```

```text
Database DOWN
     ↓
Overall DEGRADED
```

---

## 🗄️ Database

The project uses **SQLite** because it is lightweight, embedded, and does not require a separate database server.

The database contains a `system_info` table with basic application information.

Example information includes:

```text
app_name
version
owner
```

The database is automatically initialized when the application starts.

---

## 📦 Dependencies

Dependencies are defined in:

```text
app/requirements.txt
```

The project uses pinned dependency versions to improve reproducibility.

The same requirements file is used during:

```text
Local Setup
     ↓
Docker Build
     ↓
Jenkins Install
```

---

## 🔐 Repository Hygiene

The project uses `.gitignore` and `.dockerignore` to prevent unnecessary or generated files from being committed or included in the Docker build context.

Examples:

```text
venv/
.jenkins-venv/
__pycache__/
.pytest_cache/
*.pyc
system_health.db
.env
.git/
```

No passwords, API tokens, credentials, private keys, or other secrets should be committed to the repository.

---

## 📊 Complete Project Workflow

```text
Developer
    ↓
Git Feature Branch
    ↓
Code Changes
    ↓
Pytest
    ↓
Merge to develop
    ↓
Jenkins
    ↓
Checkout
    ↓
Install Dependencies
    ↓
Run Tests
    ↓
Build Docker Image
    ↓
Tag Image
    ↓
Run Temporary Container
    ↓
Health Check
    ↓
Remove Container
    ↓
Successful CI Pipeline
    ↓
develop → main
```

---

## 🎯 Project Objective

The objective of this project is to demonstrate a basic SRE/DevOps workflow where application code is developed using Git, tested automatically using Pytest, packaged using Docker, and continuously validated through Jenkins.

The project combines application health monitoring with CI automation to ensure that the application is tested before the Docker image is considered valid.

---

## 🤖 AI Assistance Disclosure

AI tools were used as a learning and development aid for concept explanations, troubleshooting, command guidance, and documentation.

The project was reviewed, executed, tested, and understood by the project author.

---

## 👤 Author

**Ashmita Barthwal**

GitHub Repository:

https://github.com/Ashmita-2026/Mini-Project-.git

