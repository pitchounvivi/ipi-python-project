import os

from flask import Flask, render_template, app

def create_app(test_config=None) :
    """create and configure the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    

    #____ROUTES____

    #homepage
    @app.route('/homepage') # URL page in the browser
    def homepage() :
        """return the homepage template"""
        return render_template('homepage.html')

    #homepage
    @app.route('/test')
    def test() :
        """return the test template"""
        return render_template('test.html')
    
    
    
    
    
    
    
    
    
    
    
    # Call init_app function from db.py
    from . import db
    db.init_app(app)
    
    return app
