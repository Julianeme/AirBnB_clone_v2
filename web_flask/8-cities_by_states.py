#!/usr/bin/python3
""" script that starts a Flask web application:
    listens on 0.0.0.0, port 5000
    Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
"""
from models import storage
from flask import Flask
from flask import render_template
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """
    Returns HBNB
    '"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardonw_appcontext(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
