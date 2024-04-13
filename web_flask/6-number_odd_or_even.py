#!/usr/bin/python3
""" A script that starts a Flask web application """
from flask import Flask, render_template

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


@app.route("/python/", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    """ A function that return python """
    return "Python" + " " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def is_num(n=0):
    """ A function that return numbers """
    return str(n) + " is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def temp_num(n):
    """ Return html """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """ Return Odd or Even """
    if n % 2 == 0:
        n = str(n) + " is even"
	return render_template("6-number_odd_or_even.html", n = n)
    if n % 2 != 0:
        n = str(n) + " is odd"
	return render_template("6-number_odd_or_even.html", n = n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
