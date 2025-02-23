#!/usr/bin/python3
''' a script that starts a Flask web application '''

from flask import Flask, render_template

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
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_index(text='is cool'):
    ''' displays python followed by value of text'''
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def num_index(n):
    '''displays n is a number only if n is an integer'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_index(n):
    '''displays n is a HTML page only if n is an integer'''
    return render_template('5-number.html', index_num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
