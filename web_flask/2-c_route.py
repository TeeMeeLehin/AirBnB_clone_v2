#!/usr/bin/python3
""" Script that starts a falsk web application"""
from flask import Flask, request
import re

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
    text = re.sub("_", " ", text)
    return (f'C {text}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
