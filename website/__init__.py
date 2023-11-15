from flask import Flask
from flask_sqlalchemy import SQLAlchemy     # import sqlalchemy...
from os import path                         # use this path module to determine if path to our db exists...
from flask_login import LoginManager


# this file will turn our overall 'website' folder into a python package...

# define and initialize our database.. then name it
db = SQLAlchemy()
DB_NAME = "database.db"     # naming our database

# we set up our flask app in this file
# function to create our flask app...
def create_app():
    app = Flask(__name__)   # initializes our app
    # create a key for our session data and cookies... this is not important for us, but a big deal with production level code in industry...
    app.config['SECRET_KEY'] = 'key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  # storing our database in our website folder (where init.py is located)
    db.init_app(app)
    
    
    # we need to register our blueprints into our init file
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note  # this will make sure we load this file with these models before we run our app
    
    # create our db this way.. not with function:
    with app.app_context():
        db.create_all()
    
    # create_database(app)
    
    # set up login manager - must be done after we set up our database..
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'     # if user is not logged in, they should view the auth.login view...
    login_manager.init_app(app)
    
    @login_manager.user_loader  # this tells flask we want to load the user by its primary key, its id
    def load_user(id):
        return User.query.get(int(id))
    
    return app

# function to create our db..
# def create_database(app):
#     if not path.exists('website/' + DB_NAME):   # if db doesnt exist, then create it
#         db.create_all(app=app)
#         print('Created Database!')
        
        