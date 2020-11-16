"""Authentification Module"""
from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register/', methods=('GET', 'POST'))
def register():
    """Register function"""
    if request.method == 'POST':
        username = request.form['username']
        lastname = request.form['lastname']
        firstname = request.form['firstname']
        email = request.form['email']
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
            'SELECT user_id FROM user WHERE user_username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (user_username, user_lastname, '
                + 'user_firstname, user_email, user_password)'
                + 'VALUES (?, ?, ?, ?, ?)',
                (username, lastname, firstname, email,
                generate_password_hash(password)))
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    """Login"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE user_username = ?', (username,)
            ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['user_password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['id'] = user['user_id']
            session['username'] = user['user_username']
            session['firstname'] = user['user_firstname']
            session['lastname'] = user['user_lastname']
            session['email'] = user['user_email']
            session['password'] = user['user_password']
            return redirect(url_for('homepage'))

        flash(error)

    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    """deconnection and clear session"""
    session.clear()
    return redirect(url_for('index'))
