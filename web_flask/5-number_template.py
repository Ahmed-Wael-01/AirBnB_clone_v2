#!/usr/bin/python3
"""basic flask app"""
from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonista(text="is cool"):
    """handle root route"""
    return "Python " + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def numbers(n):
    """handle root route"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_page(n):
    """handle root route"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
