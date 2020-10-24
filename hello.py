"""Module Flask"""
#the compliance checker with pep8 (pylint) requires me to have a comment before imports
from flask import Flask
app = Flask(__name__)


"""routing homepage"""
@app.route('/')

def hello_world():
    """display test"""
    return 'Hello, World! ici'
