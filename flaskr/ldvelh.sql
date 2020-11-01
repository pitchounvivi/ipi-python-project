--
-- Fichier généré par SQLiteStudio v3.2.1 sur dim. nov. 1 10:40:51 2020
--
-- Encodage texte utilisé : System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

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
    user_firstname VARCHAR (50)  NOT NULL,
    user_lastname  VARCHAR (50)  NOT NULL,
    user_email     VARCHAR (150) NOT NULL,
    user_password  VARCHAR (20)  NOT NULL
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
