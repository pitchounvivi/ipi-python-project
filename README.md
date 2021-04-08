==============================

# ipi-python-project

==============================

# Outils et aide

-Trello : https://trello.com/b/W5tq8VA7/projet-python
- VS Code : penser à ajouter les extensions (le shell launcher pour avoir plusieurs terminaux et french language)

pour Python, Jupyter qui facilite bien la vie !
et dans le cadre de ce projet : SQLite.

==============================

## Récupérer le projet Github avec Git
* Dans le dossier que vous souhaitez : 

Ouvrez un terminal Bash
```terminal Bash
git clone adresse_url_du_projet_github
```

==============================

## Procédure pour créer l'environnement virtuel
* Aller dans le dossier du projet

* Ouvrir l'invite de commande windows dans le projet Python : 

    **Astuce : dans le chemin d'accès au dossier, taper directement : cmd

* Créer le venv dans le projet Github
```terminal
py -3 -m venv venv
```

==============================

## Procédure pour lancer l'environnement virtuel
* Activer l'environnement virtuel
```terminal
venv\Scripts\activate
```

==============================

## Procédure pour lancer le programme en local
* Installer les différents modules
```terminal
pip install -r requirements.txt
```

* Lier les variables du package :
```terminal
set FLASK_APP=flaskr
```

* Mode debug :
```terminal
set FLASK_ENV=development
```

* Initialisation de la bdd : 
```terminal
flask init-db
```

* Lancer le serveur :
```terminal
flask run
```

==============================

## Utiliser le programme
* Ouvrez votre navigateur préféré à l'adresse :
http://127.0.0.1:5000/

*  Voilà votre programme est désormais lancé !

BONNE LECTURE