"""Gamebook application."""
import os

from flask import Flask, render_template, request, session, url_for, redirect

from . import auth
from . import book
from .db import get_db, init_app


def create_app(test_config=None):
    """Create and configure the app."""
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

    @app.route('/')
    def index():
        """Index page."""
        return render_template('index.html')

    @app.route('/homepage/')
    def homepage():
        """Homepage."""
        if "username" in session:
            username = session['username']
        db = get_db()
        books = db.execute('SELECT * FROM book').fetchall()
        db.commit()
        username = session['username']
        return render_template('homepage.html', books=books, username=username)

    @app.route('/profil/', methods=('GET', 'POST'))
    def profil():
        """Profile page and update."""
        if session:
            username = session['username']
            firstname = session['firstname']
            lastname = session['lastname']

        if request.method == 'POST':
            user_id = session['id']
            username = request.form['username']
            firstname = request.form['firstname']
            lastname = request.form['lastname']

            db = get_db()
            db.execute(
                'UPDATE user SET user_username = ?, '
                'user_firstname = ?, user_lastname = ? WHERE user_id = ?',
                (username, firstname, lastname, user_id))
            db.commit()

            # Update session
            session['id'] = user_id
            session['username'] = username
            session['firstname'] = firstname
            session['lastname'] = lastname
            return redirect(url_for('homepage'))

        return render_template(
            'profil.html', username=username, firstname=firstname,
            lastname=lastname)

    # Initialize DataBase
    init_app(app)

    # Loading the path of authentication routes
    app.register_blueprint(auth.bp)
    app.register_blueprint(book.bp)

    return app
