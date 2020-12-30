"""Authentication module."""

from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from .db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register/', methods=('GET', 'POST'))
def register():
    """Register page."""
    if request.method == 'POST':
        username = request.form['username']
        lastname = request.form['lastname']
        firstname = request.form['firstname']
        email = request.form['email']
        password = request.form['password']

        db = get_db()
        if db.execute(
            'SELECT user_id FROM user WHERE user_username = ?', (username,)
        ).fetchone() is not None:
            flash('User {} is already registered.'.format(username))
            return redirect(url_for('auth.register'))

        db.execute(
            'INSERT INTO user (user_username, user_lastname, '
            'user_firstname, user_email, user_password)'
            'VALUES (?, ?, ?, ?, ?)', (
                username, lastname, firstname, email,
                generate_password_hash(password)))
        db.commit()
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@bp.route('/login/', methods=('GET', 'POST'))
def login():
    """Login page."""
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
        else:
            session.clear()
            session['id'] = user['user_id']
            session['username'] = user['user_username']
            session['firstname'] = user['user_firstname']
            session['lastname'] = user['user_lastname']
            session['email'] = user['user_email']
            session['password'] = user['user_password']
            return redirect(url_for('homepage'))

        flash(error)
        return redirect(url_for('auth.login'))

    return render_template('auth/login.html')


@bp.route('/logout', methods=('POST',))
def logout():
    """Logout page clearing session."""
    session.clear()
    return redirect(url_for('index'))
