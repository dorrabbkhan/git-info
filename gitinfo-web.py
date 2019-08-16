"""
Runs a Flask webserver which allows you to view information about a Github
repository, which is obtained using the gitinfo.Repository class. Depends on
the flask package, and the gitinfo module. Will dynamically add new 
information based on the available functions of said class.
"""

from flask import Flask, render_template, request
from gitinfo import repository

APP = Flask(__name__)
DATA = []
# initialize Flask app, list of dictionaries

@APP.route("/")
def index():
    """
    Index page which renders any information given to it.
    """

    return render_template("index.html", repo_data=DATA)

@APP.route("/get_data", methods=["POST"])
def get_data():
    """
    Gets the repo data, formats it into data, renders the index page.
    """

    url = request.form['url']
    # gets the URL from the input box on index.html

    try:
        DATA.clear()
        # empties the list

        repo = repository(url)
        for name in [
                function for function in dir(repo)
                if not function.startswith("_")
                and callable(getattr(repo, function))
            ]:
            # only public functions from repo object used
            # by selecting attributes which do
            # not start with _ and are callable

            datum = {
                "name": name,
                "info": getattr(repo, name)()
            }
            # format required by index.html

            DATA.append(datum)
            # append to data to be displayed on index.html

    except Exception as error:
        # in case of errors, tells the client

        DATA.append({
            "name": "Error",
            "info": error
        })
        # append to data to be displayed on index.html

    return index()
    # return data to the webpage

APP.run(host="127.0.0.1", port=5000, debug=True)
# runs the webserver locally in debug mode (which presents errors prettily)
