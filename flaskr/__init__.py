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

    @app.route('/login/')
    def login():
        """login"""
        return render_template('auth/login.html')

    @app.route('/register/', methods=('GET', 'POST'))
    def register():
        """register"""
        if request.method == 'POST':
            username = request.form['username']
            lastname = request.form['lastname']
            firstname = request.form['firstname']
            email = request.form.get('email')
            password = request.form['password']
            db = get_db()
            error = None

            if not username:
                error = 'Username is required.'
            elif not lastname:
                error = 'Lastname is required.'
            elif not firstname:
                error = 'Firstname is required.'
            elif not email:
                error = 'Email is required.'    
            elif not password:
                error = 'Password is required.'
            elif db.execute(
                'SELECT id FROM user WHERE user_username = ?', (username,)
            ).fetchone() is not None:
                error = 'User {} is already registered.'.format(username)

            if error is None:
                db.execute(
                    'INSERT INTO user (user_username, user_lastname, user_firstname, user_email, user_password) VALUES (?, ?, ?, ?, ?)',
                    (username, lastname, firstname, email, generate_password_hash(password))
                )
                db.commit()
                return redirect(url_for('login'))
            
            flash(error)

        return render_template('auth/register.html')

    @app.route('/homepage')
    def homepage():
        """homepage"""
        lastname = request.args.get('lastname')
        firstname = request.args.get('firstname')
        return render_template('homepage.html',
                                lastname=lastname,
                                firstname=firstname)
        return render_template('homepage.html')




    
    
    
    
    # Call init_app function from db.py
    from . import db
    db.init_app(app)
    
    return app

    # Call auth.bp function from auth.py
    from . import auth
    app.register_blueprint(auth.bp)

    return app
