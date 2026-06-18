
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Welcome to the Flask Virtual Diner!"
    }
