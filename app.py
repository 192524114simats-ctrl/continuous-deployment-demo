from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello! Welcome to my CI/CD application.",
        "application": "Flask Web App",
        "containerization": "Docker",
        "ci_cd_tool": "GitHub Actions",
        "container_registry": "Docker Hub",
        "cloud_platform": "Render",
        "deployment_status": "Successful"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)