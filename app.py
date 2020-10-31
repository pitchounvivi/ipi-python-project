#! /usr/bin/env python3 #ligne pour l'interpréteur Python
# coding: utf-8

"""Flask Module"""
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

# Config options
app.config.from_object('config')

@app.route('/')
def index():
    """index"""
    return render_template('index.html')

@app.route('/login/')
def login():
    """login"""
    return render_template('login.html')

@app.route('/register/')
def register():
    """register"""
    return render_template('register.html')

@app.route('/homepage/')
def homepage():
    """homepage"""
    pseudo = request.args.get('pseudo')
    return render_template('homepage.html',
                            pseudo=pseudo)


if __name__ == "__main__":
    app.run(debug=True)
 