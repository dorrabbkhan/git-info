"""
Runs a Flask webserver which allows you to view information about a Github 
repository, which is obtained using the gitinfo.Repository class. Depends on 
the flask package, and the gitinfo module. Will dynamically add new information
based on the available functions of said class.
"""
from flask import Flask, render_template, request
from gitinfo import Repository

app = Flask(__name__)

data = [] # list of dictionaries

@app.route("/")
def index():
    """
    Index page which renders any information given to it.
    """
    return render_template("index.html", repo_data=data)

# logic for 
@app.route("/get_data", methods=["POST"])
def get_data():
    """
    Gets the repo data, formats it into data, renders the index page.
    """
    while len(data) != 0: data.pop() # empties the list
    url = request.form['url'] # gets the URL from the input box on index.html
    if not url.startswith("https://www.github.com/"):
        url = "https://www.github.com/" + url # allows 'user/repo' format
    try:
        repo = Repository(url)
        for name in [d for d in dir(repo) if not d.startswith("_") 
            and callable(getattr(repo, d))]: 
            # only public functions used
            datum = { # format required by index.html
                "name": name,
                "info": eval("repo."+name+"()")
            }
            data.append(datum)
    except Exception as e: # in case of errors, tells the client
        data.append({
            "name": "Error",
            "info": e
        })
    finally:
        return index()

# runs the webserver locally in debug mode (which presents errors prettily)
app.run(host="127.0.0.1", port=5000, debug=True) 