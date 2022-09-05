#!/usr/bin/python3
""" Flask web application """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ remove the current SQLAlchemy Session """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Render a particular state """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    users = storage.all("User")
    return render_template(
        '100-hbnb.html',
        states=states, amenities=amenities, places=places, users=users
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
