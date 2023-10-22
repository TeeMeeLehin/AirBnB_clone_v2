#!/usr/bin/python3
""" Script that starts a falsk web application"""
from flask import Flask, request, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    " function to remove surrent SQLAlchemy session "
    storage.close()


@app.route('/states', strict_slashes=False)
def states_lists():
    " function to display all states in storage "
    state_d = storage.all(State)
    states = list(sorted(state_d.values(), key=lambda value: value.name))

    return (render_template("9-states.html", states=states))


@app.route('/states/<id>', strict_slashes=False)
def states_cities(id):
    " function to display all cities in specified state "
    state_d = storage.all(State)
    states = list(sorted(state_d.values(), key=lambda value: value.name))

    for state in states:
        if (state.id == id):
            stat = state
            break
        else:
            stat = None

    return (render_template("9-states.html", stat=stat))        


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
