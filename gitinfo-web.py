from flask import Flask, render_template, request
from gitinfo import Repository

app = Flask(__name__)

data = [] # list of dictionaries

@app.route("/")
def index():
    return render_template("index.html", data=data)

@app.route("/get_data", methods=["POST"])
def get_data():
    url = request.form['url']
    repo = Repository(url)
    for name, info in enumerate([d for d in dir(repo) if not d.startswith("__")]): # all magic methods excluded
        datum = {
            "name": name,
            "info": info
        }
        data.append(datum)
    return index()

app.run(host="127.0.0.1", port=5000, debug=True) 