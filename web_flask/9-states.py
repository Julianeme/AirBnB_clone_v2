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


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    Returns list of all State objects present
    in DBStorage sorted by name (A->Z)
    '"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """
    Shows a state searched by id and all its cities
    '"""
    states = storage.all(State)
    id = 'State.' + id
    for keys, values in states.items():
        if states[keys] == id:
            name = values.name
            return render_template(
                "9-states.html", name=name, states=states, id=id)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardonw_appcontext(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
