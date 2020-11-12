"""Book Module"""

from flask import (
    Blueprint, render_template, request, redirect, url_for
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

@bp.route('/book/<book_id>/page/', defaults={'page_id': 0}, methods=('GET', 'POST'))
@bp.route('/book/<book_id>/page/<page_id>/', methods=('GET', 'POST'))
def page(book_id,page_id):
    """displays a page according to the book and the requested page"""
    if request.method == 'POST':
        choose = request.form['choix']
        book = request.form['book']
        return redirect(url_for('bookstore.page', book_id=book, page_id=choose,))

    if page_id == 0:
        db = get_db()
        book = db.execute(
            'SELECT * FROM book JOIN chapter WHERE chapter.chap_id = book.book_first_chap '
            + ' AND book.book_id = ?',(book_id,)).fetchone()
        db.commit()
        return render_template('bookstore/page.html', book=book)

    db = get_db()
    book = db.execute(
        'SELECT * FROM book JOIN chapter WHERE chapter.book_id = book.book_id '
        + ' AND chapter.chap_id = ? '
        + ' AND book.book_id = ? ',(page_id,book_id,)).fetchone()
    db.commit()

    return render_template('bookstore/page.html', book=book)

@bp.route('/book/reading/')
def reading():
    return render_template('bookstore/reading.html')
    