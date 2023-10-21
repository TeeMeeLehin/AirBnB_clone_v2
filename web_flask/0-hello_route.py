#!/usr/bin/python3
""" Script that starts a falsk web application"""
from flask import Flask, request

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    " function to say hello "
    return ('Hello HBNB!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
