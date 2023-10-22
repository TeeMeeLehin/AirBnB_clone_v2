#!/usr/bin/python3
""" Script that starts a falsk web application"""
from flask import Flask, request, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    " function to remove surrent SQLAlchemy session "
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    " function to display a hbnb html page "
    state_d = storage.all(State)
    states = list(sorted(state_d.values(), key=lambda value: value.name))

    city_d = storage.all(City)
    cities = list(sorted(city_d.values(), key=lambda value: value.name))

    amenity_d = storage.all(Amenity)
    amenities = list(sorted(amenity_d.values(), key=lambda value: value.name))

    place_d = storage.all(Place)
    places = list(sorted(place_d.values(), key=lambda value: value.name))

    return (render_template("100-hbnb.html", states=states, places=places, amenities=amenities))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
