# our views
# most views will go in here, views not related to authentication and routes that users can navigate to
from flask import Blueprint, render_template

# a blueprint simply means that this file, views.py, should contain routes...
views = Blueprint('views', __name__)     # this defines the name of our blueprint and sets up our blueprint for our app (we'll do same in auth.py)


@views.route('/')   # defining our home page route (this is a constructor)
def home():         # whatever is in our home funciton, will run when we go to the '/' route
    return render_template("home.html")

