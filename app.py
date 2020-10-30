#! /usr/bin/env python3 #ligne pour l'interpréteur Python
# coding: utf-8

"""Flask"""
from flask import Flask, render_template

app = Flask(__name__)

"""routing"""
@app.route('/')

def index():
    """homepage"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
 