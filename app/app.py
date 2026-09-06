from flask import Flask
import os

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)