#! /usr/bin/env python3 #ligne pour l'interpréteur Python
# coding: utf-8

"""Application Module"""
import os

from flask import Flask, render_template, app, request, session
from werkzeug.security import check_password_hash

from flaskr.db import get_db

# Call init_app function from db.py
from . import db

# Call auth.bp function from auth.py
from . import auth
# Call book.bp function from book.py
from . import book


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
            username = session['username']
        db = get_db()
        books = db.execute('SELECT * FROM book').fetchall()
        db.commit()
        username = session['username']
        return render_template('homepage.html', books=books, username=username)

    @app.route('/profil/', methods=('GET', 'POST'))
    def profil():
        """profil and update profil"""
        if session:
            username = session['username']            
            firstname = session['firstname']
            lastname = session['lastname']
            email = session['email']
            passw = session['password']

        if request.method == 'POST':
            user_id = session['id']
            username = session['username'] if None else request.form.get('username')
            firstname = session['firstname'] if None else request.form.get('firstname')
            lastname = session['lastname'] if None else request.form.get('lastname')

            # To Do: Finir la fonction, régler le problème de Type concernant le mot de passe 
            # new_mail = request.form.get('new_mail')
            # mail_confirm = request.form.get('mail_confirm')
            # new_password = request.form.get('new_password')
            # password_confirm = request.form.get('password_confirm')
            # password = request.form.get('password')

            # if new_mail == mail_confirm and mail_confirm != None :
            #     email = mail_confirm
            #     username = session['username']
            #     firstname = session['firstname']
            #     lastname = session['lastname']
            
            # if check_password_hash(passw, password):
            #     if new_password == password_confirm and password_confirm != None:
            #         password = password_confirm
            #         username = session['username']
            #         firstname = session['firstname']
            #         lastname = session['lastname']

        #     db = get_db()
        #     user = db.execute('UPDATE user SET user_username = ?, user_firstname = ?, user_lastname = ?, user_email = ?, user_password = ? WHERE user_id = ?', (username, firstname, lastname, email, password, user_id,))
        #     db.commit()
        # return render_template('profil.html', username=username, firstname=firstname, lastname=lastname, email=email)


            db = get_db()
            user = db.execute('UPDATE user SET user_username = ?, user_firstname = ?, user_lastname = ? WHERE user_id = ?', (username, firstname, lastname, user_id,))
            db.commit()
        return render_template('profil.html', username=username, firstname=firstname, lastname=lastname,)
    
    # Initialize DataBase
    db.init_app(app)

    # Loading the path of authentication routes
    app.register_blueprint(auth.bp)
    app.register_blueprint(book.bp)

    return app
