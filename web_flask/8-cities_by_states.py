#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def citiesList():
    '''return the cities by states'''
    states = sorted(list(storage.all('State').values()), key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardownStorage(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
