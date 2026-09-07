from flask import Flask
import os
import sys
import time
import psutil
START_TIME = time.time()

app = Flask(__name__)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.database import initialize_database, get_system_info, check_database

@app.get("/health")
def health():
    return {"status": "UP"}


@app.get("/version")
def version():
    return {"version": os.getenv("APP_VERSION", "1.0.0")}


@app.get("/environment")
def environment():
    return {"environment": os.getenv("APP_ENV", "development")}


@app.get("/services")
def services():
    return {
        "services": [
            {
                "name": "API",
                "technology": "Flask"
            },
            {
                "name": "Database",
                "technology": "PostgreSQL"
            }
        ]
    }
    
initialize_database()


@app.get("/database/health")
def database_health():
    return {"database": check_database()}


@app.get("/database/info")
def database_info():
    return get_system_info()


@app.get("/services/status")
def services_status():
    services = [
        {
            "name": "API",
            "status": "UP"
        },
        {
            "name": "Database",
            "status": check_database()
        }
    ]

    return {
        "services": services,
        "total_services": len(services)
    }
    
@app.get("/system/summary")
def system_summary():
    database_status = check_database()

    services = [
        {"name": "API", "status": "UP"},
        {"name": "Database", "status": database_status}
    ]

    overall_status = "UP" if database_status == "UP" else "DEGRADED"

    return {
        "overall_status": overall_status,
        "environment": os.getenv("APP_ENV", "development"),
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "database": database_status,
        "services": len(services),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "uptime_seconds": round(time.time() - START_TIME, 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)