==============================

# ipi-python-project

==============================

Trello
https://trello.com/b/W5tq8VA7/projet-python

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

* Ouvrir l'invite de commande windows dans le projet Python
Comme  : 

Par exemple dans le chemin d'accès au dossier, taper directement : cmd

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

## Procédure pour lancer le programme
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
set FLASK_ENV=developement
```

* Initialisation de la bdd : 
```terminal
flask init-db
```

* Lancer le serveur :
```terminal
flask run
```
