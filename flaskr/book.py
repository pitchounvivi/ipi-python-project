"""Book Module"""
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('bookstore', __name__, url_prefix='/bookstore')

    
@bp.route('/book/')
def book():
    """Display function"""
    # db = get_db()
    # book = db.execute('SELECT * FROM book WHERE id = ?',(book_id,)).fetchone()
    # db.commit()
    # return redirect(url_for('bookstore/book.html',book=book))
    return render_template('bookstore/book.html')
    