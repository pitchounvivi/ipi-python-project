PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

------------------------------------------------------------------
-- Creation area of the different tables
------------------------------------------------------------------

-- Table : book
DROP TABLE IF EXISTS book;

CREATE TABLE book (
    book_id         INTEGER       PRIMARY KEY AUTOINCREMENT,
    book_title      VARCHAR (255),
    book_resume     VARCHAR (255),
    book_first_chap INTEGER (11)  REFERENCES chapter (chap_id)
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
INSERT INTO book (book_title, book_resume, book_first_chap)
 VALUES
 ('Promenade en forêt', 'Une histoire de promenade en forêt', 1),
 ('Super Héros and Co', 'Une compagnie de super héros', 9),
 ('Bizarre vous avez dit bizarre', 'Etrangetés et autres situations bizarre', 10)
;


-- Table : chapter
-- First book
INSERT INTO chapter (chap_title, chap_content, book_id)
 VALUES
 ('Chap 1 : début',
 '<p>une super histoire</p> 
 <form method="POST"> 
 <label for="2">Vous voulez allez au 2</label>
 <input type="radio" name="choix" value="2" />
 <label for="4">Vous voulez allez au 4</label>
 <input type="radio" name="choix" value="4" />
 <input type="submit" value="Valider"/>
 </form>', 
 1)
;
INSERT INTO chapter (chap_title, chap_content, book_id)
 VALUES
 ('Chap 2 : suite *',
 '<p>un bout d''histoire</p>
 <form method="POST"> 
 <label for="3">Vous voulez allez au 3</label>
 <input type="radio" name="choix" value="3" />
 <label for="5">Vous voulez allez au 5</label>
 <input type="radio" name="choix" value="5" />
 <input type="submit" value="Valider"/>
 </form>', 
 1)
;
INSERT INTO chapter (chap_title, chap_content, book_id)
 VALUES
 ('Chap 3 : suite **',
 '<p>un autre bout d''histoire</p>
 <form method="POST"> 
 <label for="7">Vous voulez allez au 7</label>
 <input type="radio" name="choix" value="7" />
 <label for="5">Vous voulez allez au 5</label>
 <input type="radio" name="choix" value="5" />
 <input type="submit" value="Valider"/>
 </form>', 
 1)
;
INSERT INTO chapter (chap_title, chap_content, book_id)
 VALUES
 ('Chap 4 : suite ***',
 '<p>un rebondissement d''histoire</p>
 <form method="POST"> 
 <label for="6">Vous voulez allez au 6</label>
 <input type="radio" name="choix" value="6" />
 <label for="8">Vous voulez allez au 8</label>
 <input type="radio" name="choix" value="8" />
 <input type="submit" value="Valider"/>
 </form>', 
 1)
;
INSERT INTO chapter (chap_title, chap_content, book_id)
 VALUES
 ('Chap 5 : suite ****',
 '<p>une étape de l''histoire</p>
 <form method="POST"> 
 <label for="3">Vous voulez allez au 3</label>
 <input type="radio" name="choix" value="3" />
 <label for="7">Vous voulez allez au 7</label>
 <input type="radio" name="choix" value="7" />
 <input type="submit" value="Valider"/>
 </form>', 
 1)
;
INSERT INTO chapter (chap_title, chap_content, book_id)
 VALUES
 ('Chap 6 : suite *****',
 '<p>une nouvelle étape de l''histoire</p>
 <form method="POST"> 
 <label for="4">Vous voulez allez au 4</label>
 <input type="radio" name="choix" value="4" />
 <label for="8">Vous voulez allez au 8</label>
 <input type="radio" name="choix" value="8" />
 <input type="submit" value="Valider"/>
 </form>', 
 1)
;
INSERT INTO chapter (chap_title, chap_content, book_id)
 VALUES
 ('Chap 7 : suite ******',
 '<p>une autre étape de l''histoire</p>
 <form method="POST"> 
 <label for="8">Vous voulez allez au 8</label>
 <input type="radio" name="choix" value="8" />
 <label for="5">Vous voulez allez au 5</label>
 <input type="radio" name="choix" value="5" />
 <input type="submit" value="Valider"/>
 </form>', 
 1)
;
INSERT INTO chapter (chap_title, chap_content, book_id)
 VALUES
 ('Chap 8 : fin',
 '<p>fin de l''histoire</p>', 
 1)
;

-- Second book
INSERT INTO chapter (chap_title, chap_content, book_id)
 VALUES
 ('Chap 1 : Début du livre 2',
 '<p>Début de l''histoire</p>', 
 2)
;

-- Third book
INSERT INTO chapter (chap_title, chap_content, book_id)
 VALUES
 ('Chap 1 : Début du livre 3',
 '<p>Début de l''histoire du livre 3</p>', 
 3)
;

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
