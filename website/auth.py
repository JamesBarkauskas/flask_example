# log in page will go here in auth because logging in is related to authentication...
# we'll need a auth blueprint too
# Blueprint is a way of containing routes... render_template will render our html templates... request will allow us to use http requests...
# flash is a function of Flask that allows us to 'flash' a message to the user based on their input...
from flask import Blueprint, render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash # allows us to  hash passwords

auth = Blueprint('auth', __name__)  # setting up and defining our auth blueprint

# within 'auth.py' we'll need our auth routes (login, logout, sign-up)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form 
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return '<p>logout</p>'

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # if method is a POST request... elif method is a GET request...
    # this is how we get the data we entered into our form
    if request.method == 'POST':
        email = request.form.get('email')           # use the get() method to grab the name of the input we declared in our html...
        firstName = request.form.get('firstName')   
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        # do validation checks...
        # we can use Flask's 'flash' method to flash error or success messages
        if len(email) < 4:
            flash('Email must be greater than three characters', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than one character', category='error')
        elif password1 != password2:
            flash('Passwords must match', category='error')
        elif len(password1) < 7:        # make sure password is of certain length...
            flash('Password must be greater than seven characters', category='error')
        else:
            # add user to database...
            flash('Account created!', category='success')
    return render_template("sign_up.html")


