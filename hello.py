#! /usr/bin/env python3 #ligne pour l'interpréteur Python

# coding: utf-8

"""Module Flask"""
#the compliance checker with pep8 (pylint) requires me to have a comment before imports
from flask import Flask
app = Flask(__name__)


"""routing homepage"""
@app.route('/')

def hello_world():
    """display Hello, World for test"""
    return 'Hello, World! ici aussi'

if __name__ == "__main__":
    app.run(debug=True)
    