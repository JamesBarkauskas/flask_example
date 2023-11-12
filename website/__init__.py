from flask import Flask

# this file will turn our overall 'website' folder into a python package...
# we set up our flask app in this file
# function to create our flask app...
def create_app():
    app = Flask(__name__)   # initializes our app
    # create a key for our session data and cookies... this is not important for us, but a big deal with production level code in industry...
    app.config['SECRET_KEY'] = 'key'
    
    # we need to register our blueprints into our init file
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app
