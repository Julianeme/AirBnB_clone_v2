#!/usr/bin/python3
""" script that starts a Flask web application:
    listens on 0.0.0.0, port 5000
    Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    Hello HBNB page
    '"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns HBNB
    '"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Returns HBNB
    '"""
    text = text.replace("_", " ")
    return 'C {}'.format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
