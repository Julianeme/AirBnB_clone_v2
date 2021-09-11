#!/usr/bin/python3
""" script that starts a Flask web application:
    listens on 0.0.0.0, port 5000
    Routes:
    /: display ?Hello HBNB!?
    /hbnb: display ?HBNB?
"""
from models import storage
from models.state import State
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Returns HBNB
    '"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardonw_appcontext(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
