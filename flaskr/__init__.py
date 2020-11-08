#! /usr/bin/env python3 #ligne pour l'interpréteur Python
# coding: utf-8

"""Application Module"""
import os

from flask import Flask, render_template, app, request, session

# Call init_app function from db.py
from . import db

# Call auth.bp function from auth.py
from . import auth


def create_app(test_config=None) :
    """create and configure the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    #____ROUTES____
    # Config options
    # app.config.from_object('config')

    @app.route('/')
    def index():
        """index"""
        return render_template('index.html')

    @app.route('/homepage/')
    def homepage():
        """homepage"""
        if "username" in session:
            pseudo = session['username']
        return render_template('homepage.html', pseudo=pseudo)

    @app.route('/profil/')
    def profil():
        """profil"""
        if session:
            username = session['username']            
            firstname = session['firstname']
            lastname = session['lastname']
            email = session['email']
        return render_template('profil.html', username=username, firstname=firstname, lastname=lastname, email=email)


    # Initialize DataBase
    db.init_app(app)

    # Loading the path of authentication routes
    app.register_blueprint(auth.bp)

    return app
