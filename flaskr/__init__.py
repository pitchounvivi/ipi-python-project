#! /usr/bin/env python3 #ligne pour l'interpréteur Python
# coding: utf-8

import os

from flask import Flask, render_template, app, request


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

    # @app.route('/login/')
    # def login():
    #     """login"""
    #     return render_template('login.html')

    # @app.route('/register/')
    # def register():
    #     """register"""
    #     return render_template('register.html')

    # @app.route('/homepage')
    # def homepage():
    #     """homepage"""
    #     # lastname = request.args.get('lastname')
    #     # firstname = request.args.get('firstname')
    #     # return render_template('homepage.html',
    #     #                         lastname=lastname,
    #     #                         firstname=firstname)
    #     return render_template('homepage.html')




    
    
    
    
    # Call init_app function from db.py
    from . import db
    db.init_app(app)
    
    return app

    # Call auth.bp function from auth.py
    from . import auth
    app.register_blueprint(auth.bp)

    return app
