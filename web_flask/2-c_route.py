#!/usr/bin/python3
"""basic flask app"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """handle root route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """handle root route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def textes(text):
    """handle root route"""
    return "C " + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
