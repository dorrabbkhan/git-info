from flask import Flask, render_template
from gitinfo import Repository

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

app.run(host="127.0.0.1", port=5000, debug=True) 