--
-- Fichier g�n�r� par SQLiteStudio v3.2.1 sur dim. nov. 1 10:40:51 2020
--
-- Encodage texte utilis� : System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

------------------------------------------------------------------
-- Creation area of the different tables
------------------------------------------------------------------

-- Table : book
DROP TABLE IF EXISTS book;

CREATE TABLE book (
    book_id    INTEGER       PRIMARY KEY AUTOINCREMENT,
    book_title VARCHAR (255) 
);


-- Table : book_user
DROP TABLE IF EXISTS book_user;

CREATE TABLE book_user (
    book_id   INTEGER (11) REFERENCES book (book_id),
    user_id   INTEGER (11) REFERENCES user (user_id),
    user_owns BOOLEAN
);


-- Table : chapter
DROP TABLE IF EXISTS chapter;

CREATE TABLE chapter (
    chap_id      INTEGER       PRIMARY KEY AUTOINCREMENT,
    chap_title   VARCHAR (255),
    chap_content TEXT,
    book_id      INTEGER (11)  REFERENCES book (book_id) 
);


-- Table : lecture
DROP TABLE IF EXISTS lecture;

CREATE TABLE lecture (
    id_user INTEGER REFERENCES user (user_id),
    chap_id INTEGER REFERENCES chapter (chap_id) 
);


-- Table : user
DROP TABLE IF EXISTS user;

CREATE TABLE user (
    user_id        INTEGER       PRIMARY KEY AUTOINCREMENT,
    user_username  VARCHAR (50)  UNIQUE NOT NULL,
    user_firstname VARCHAR (50)  NOT NULL,
    user_lastname  VARCHAR (50)  NOT NULL,
    user_email     VARCHAR (150) NOT NULL,
    user_password  VARCHAR (20)  NOT NULL
);


------------------------------------------------------------------
-- Area for filling tables for the site
------------------------------------------------------------------

-- Table : book
INSERT INTO book (book_title)
 VALUES
 ('Promenade en forêt'),
 ('Super Héros and Co'),
 ('Bizarre vous avez dit bizarre')
;


INSERT INTO chapter (chap_title, chap_content, book_id)
 VALUES
 ('chap 1 : début'),
 ('une super histoire'), 
 (1)
;


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
