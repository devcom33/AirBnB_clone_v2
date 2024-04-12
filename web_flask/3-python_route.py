#!/usr/bin/python3
""" A script that starts a Flask web application """
from flask import Flask

""" __name__ means name of module"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ A function that return Hello HBNB """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ A function that return HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """ A function that return c """
    return "C" + " " + text.replace("_", " ")


@app.route("/python/<text>", strict_slashes=False)
def c_is_fun(text = "is cool"):
    """ A function that return python """
    return "Python" + " " + text.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
