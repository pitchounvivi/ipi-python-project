"""Book Module"""

from flask import (
    Blueprint, render_template
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('bookstore', __name__, url_prefix='/bookstore')

@bp.route('/book/<book_id>/')
def book(book_id):
    """Display one book"""
    db = get_db()
    book = db.execute('SELECT * FROM book WHERE book_id = ?',(book_id,)).fetchone()
    db.commit()
    if book is None:
        abort(404)

    return render_template('bookstore/book.html', book=book)

@bp.route('/book/<book_id>/page/')
def page(book_id):
    """Display one page"""
    db = get_db()
    book = db.execute(
        'SELECT * FROM book WHERE book_id = ?',(book_id,)).fetchone()
    
    chap = db.execute(
        'SELECT * FROM book JOIN chapter WHERE chapter.book_id = book.book_id '
        + ' AND book.book_id = ?',(book_id,)).fetchone()
    db.commit()
    return render_template('bookstore/page.html', book=book, chap=chap)
