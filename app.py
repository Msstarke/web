# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from my Flask app!"

if __name__ == '__main__':
    app.run()