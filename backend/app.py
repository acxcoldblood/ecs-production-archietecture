from flask import Flask, jsonify
from datetime import datetime



import os

app = Flask(__name__)

# Basic CORS handling to allow frontend to communicate
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/')
def index():
    return jsonify({
        "status": "success",
        "message": "Backend is running",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
