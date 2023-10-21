#!/usr/bin/python3
""" Script that starts a falsk web application"""
from flask import Flask, request, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    " function to remove surrent SQLAlchemy session "
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_lists():
    " function to display all states in storage "
    state_d = storage.all(State)
    states = list(sorted(state_d.values(), key=lambda value: value.name))

    return (render_template("7-states_list.html", states=states))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
