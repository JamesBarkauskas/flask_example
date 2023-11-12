# log in page will go here in auth because logging in is related to authentication...
# we'll need a auth blueprint too
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)  # setting up and defining our auth blueprint

# within 'auth.py' we'll need our auth routes (login, logout, sign-up)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return '<p>logout</p>'

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")


