#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    '''prints Hello HBNB!'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    '''prints HBNB'''
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    '''prints C plus the content of text'''
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
