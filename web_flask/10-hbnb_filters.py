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


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Shows a state searched by id and all its cities
    '"""
    return render_template("6-index.html", name=name, states_dict=states_dict)


@app.teardown_appcontext
def teardonw_appcontext(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
