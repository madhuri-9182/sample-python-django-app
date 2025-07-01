from flask import Flask, jsonify
from dotenv import load_dotenv
import os

# Load from .env file
load_dotenv(dotenv_path="/srv/my-python-app/.env")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET', 'default-secret')
ENV = os.getenv('ENVIRONMENT', 'development')

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the secure Flask app!",
        "environment": ENV
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    
