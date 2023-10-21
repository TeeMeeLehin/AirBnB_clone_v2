#!/usr/bin/python3
""" Script that starts a falsk web application"""
from flask import Flask, request

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    " function to say hello "
    return ('Hello HBNB!')

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    " function to say hnbn "
    return ('HBNB')

@app.route('/c/<text>', strict_slashes=False)
def state_text(text):
    " function to state given text "
    text = text.replace("_", " ")
    return (f'C {text}')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is_cool"):
    " function to state given text "
    text = text.replace("_", " ")
    return (f'Python {text}')

@app.route('/number/<int:n>', strict_slashes=False)
def is_num(n):
    " function to state given integer "
    return (f"{n} is a number")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
