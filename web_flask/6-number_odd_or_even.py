#!/usr/bin/python3
""" Script that starts a falsk web application"""
from flask import Flask, request, render_template

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

@app.route('/number_template/<int:n>', strict_slashes=False)
def is_number(n):
    " function to render number template "
    return (render_template("5-number.html", n=n))

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def is_odd_or_even(n):
    " function to render number template "
    if (n % 2 == 0):
        stat = "even"
    else:
        stat = "odd"
    return (render_template("6-number_odd_or_even.html", n=n, stat=stat))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
