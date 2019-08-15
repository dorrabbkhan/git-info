from flask import Flask
from gitinfo import Repository

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Github"

app.run(host="127.0.0.1", port=5000, debug=True) 