"""Book Module"""
from flask import (
    Blueprint, render_template, request, redirect, url_for, session
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('bookstore', __name__, url_prefix='/bookstore')


@bp.route('/book/<book_id>/')
def book(book_id):
    """Display one book"""
    db = get_db()
    book = db.execute('SELECT * FROM book WHERE book_id = ?',
        (book_id,)).fetchone()
    db.commit()
    if book is None:
        abort(404)

    return render_template('bookstore/book.html', book=book)

@bp.route('/book/<book_id>/page/', defaults={'page_id': 0},
    methods=('GET', 'POST'))
@bp.route('/book/<book_id>/page/<page_id>/', methods=('GET', 'POST'))
def page(book_id,page_id):
    """displays a page according to the book and the requested page"""
    if request.method == 'POST':
        choose = request.form['choix']
        book = request.form['book']
        return redirect(url_for('bookstore.page',book_id=book, page_id=choose,))

    user_id = session['id']

    if page_id == 0:
        db = get_db()
        #par défaut, on affiche la première page du livre
        book = db.execute(
            'SELECT * FROM book JOIN chapter '
            + ' WHERE chapter.chap_id = book.book_first_chap '
            + ' AND book.book_id = ?',(book_id,)).fetchone()

        #dans le cas où il s'agit d'une relecture depuis le début
        # alors que le livre a déjà été commencé une première fois
        #on regarde s'il y a déjà ce livre pour le user
        if db.execute(
            'SELECT book_id FROM lecture WHERE user_id = ? AND book_id = ?',
            (user_id,book_id)).fetchone() is None:
            #s'il n'y est pas, on insert les informations de lecture
            db.execute(
                'INSERT INTO lecture (user_id, book_id, chap_id)'
                + 'VALUES (?, ?, ?)',(user_id, book_id,
                book['book_first_chap'],))

        #sinon on met seulement à jour
        else:
            db.execute(
                'UPDATE lecture SET chap_id = ?'
                + 'WHERE user_id = ? AND book_id = ?',(book['book_first_chap'],
                user_id, book_id,))

        db.commit()
        return render_template('bookstore/page.html', book=book)

    #on affiche la page demandée et on met à jour la table lecture
    db = get_db()
    book = db.execute(
        'SELECT * FROM book JOIN chapter WHERE chapter.book_id = book.book_id '
        + ' AND chapter.chap_id = ? '
        + ' AND book.book_id = ? ',(page_id,book_id,)).fetchone()

    db.execute(
        'UPDATE lecture SET chap_id = ?'
        + 'WHERE user_id = ? AND book_id = ? ', (page_id, user_id, book_id,))

    db.commit()

    return render_template('bookstore/page.html', book=book)

@bp.route('/book/reading/', methods=('GET', 'POST'))
def reading():
    """possibility of resuming a book in progress"""
    username = session['username']
    user = session['id']

    if request.method == 'POST':
        choose = request.form['choix']
        book = request.form['book']
        return redirect(url_for('bookstore.page',book_id=book, page_id=choose,))

    db = get_db()
    books = db.execute('SELECT * FROM lecture '
        + ' INNER JOIN book ON book.book_id = lecture.book_id '
        + ' INNER JOIN chapter ON chapter.chap_id = lecture.chap_id '
        + ' AND user_id = ?', (user,)).fetchall()

    not_book=False

    if len(books) == 0:
        not_book=True

    return render_template('bookstore/reading.html',
        username=username, books=books, not_book=not_book)
