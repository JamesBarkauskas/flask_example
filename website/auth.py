# log in page will go here in auth because logging in is related to authentication...
# we'll need a auth blueprint too
# Blueprint is a way of containing routes... render_template will render our html templates... request will allow us to use http requests...
# flash is a function of Flask that allows us to 'flash' a message to the user based on their input...
# redirect and url_for will allow us to redirect user to home page after account creation

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash # allows us to  hash passwords
from . import db    # must import the database in order to push new users into database...
from flask_login import login_user, login_required, logout_user, current_user   # current_user allows us to keep track of current user


auth = Blueprint('auth', __name__)  # setting up and defining our auth blueprint

# within 'auth.py' we'll need our auth routes (login, logout, sign-up)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # if the user is attempting to sign in.. that would be a post request.. then grab the data they entered
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # we then want to check if that data is valid.. (if that user exists in database)
        # we can filter thru the database by email
        user = User.query.filter_by(email=email).first()
        if user:                                                # if user exists.. check if the password is correct
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)                 # this will rememeber who is logged in until you restart the web server
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required         # adding a decorator, so the user cannot access this page unless they're logged in
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # if method is a POST request... elif method is a GET request...
    # this is how we get the data we entered into our form
    if request.method == 'POST':
        email = request.form.get('email')           # use the get() method to grab the name of the input we declared in our html...
        first_name = request.form.get('firstName')   
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        # do validation checks...
        # we can use Flask's 'flash' method to flash error or success messages
        user = User.query.filter_by(email=email).first()        # checking if email already exists
        if user:
            flash('Email alredy exists', category='error')
        elif len(email) < 4:
            flash('Email must be greater than three characters', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than one character', category='error')
        elif password1 != password2:
            flash('Passwords must match', category='error')
        elif len(password1) < 7:        # make sure password is of certain length...
            flash('Password must be greater than seven characters', category='error')
        else:
            # add user to database...
            # this will hash the password, with a hashing algorithm(sha256)
            new_user = User(email = email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            
            # then we need to actually add new_user to database..
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))          # redirecting to the blueprint, views, and the function of 'home.html'
    return render_template("sign_up.html", user=current_user) 


