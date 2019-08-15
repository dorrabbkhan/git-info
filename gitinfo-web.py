from flask import Flask, render_template, request
from gitinfo import Repository

app = Flask(__name__)

data = [] # list of dictionaries

@app.route("/")
def index():
    return render_template("index.html", repo_data=data)

@app.route("/get_data", methods=["POST"])
def get_data():
    url = request.form['url']
    try:
        repo = Repository(url)
        for name in [d for d in dir(repo) if not d.startswith("_") and not "url" in d]: # all magic/private methods excluded
            datum = {
                "name": name,
                "info": eval("repo."+name+"()")
            }
            data.append(datum)
    except Exception as e:
        data.append({
            "name": "Error",
            "info": e
        })
    finally:
        return index()

app.run(host="127.0.0.1", port=5000, debug=True) 