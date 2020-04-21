#!/usr/bin/python3

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    '''prints Hello HBNB!'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    '''prints HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cRoute(text):
    '''prints C plus the content of text'''
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonRoute(text='is cool'):
    '''prints Python plus the content of text'''
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def numberRoute(n):
    '''prints Python plus the content of text'''
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def numberTemplate(n):
    '''returns the number template'''
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
