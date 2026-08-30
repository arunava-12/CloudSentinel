from flask import Flask, jsonify, render_template
from datetime import datetime
import os
import time

app = Flask(__name__)

START_TIME = time.time()
VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


@app.route("/")
def home():
    uptime = int(time.time() - START_TIME)

    return render_template(
        "index.html",
        version=VERSION,
        environment=ENVIRONMENT,
        uptime=uptime
    )


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "version": VERSION,
        "environment": ENVIRONMENT
    }), 200


@app.route("/api/info")
def info():
    return jsonify({
        "application": "CloudSentinel",
        "version": VERSION,
        "environment": ENVIRONMENT,
        "status": "running",
        "uptime_seconds": int(time.time() - START_TIME),
        "timestamp": datetime.utcnow().isoformat()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)