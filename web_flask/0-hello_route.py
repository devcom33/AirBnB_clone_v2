#!/usr/bin/python3
""" First Hello in Flask """
from flask import Flask

""" __name__ means name of module"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
	""" A function that return HBNB """
	return "Hello HBNB!"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
