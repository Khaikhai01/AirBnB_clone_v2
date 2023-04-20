#!/usr/bin/python3
''' a script that starts a Flask web application '''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def file_index():
    '''a functuion that returns hello HBNB'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_index():
    ''' function that returns HBNB '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text_index(text):
    '''dispalys C followed by the value of the text'''
    new_text = text.replace("_", " ")
    return f'C {new_text}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_index(text='is cool'):
    ''' displays python followed by value of text'''
    new_text = text.replace('_', ' ')
    return f'Python {new_text}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
