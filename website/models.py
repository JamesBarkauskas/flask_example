# store our database models 
from . import db    # from our current folder.. import our db variable (the database object we created)
from flask_login import UserMixin   # helps us log users in
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now) # func.now will set the current time/date and store that as date
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))       # grabs the 'id' from User class and uses that as its foreign key

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # id will be User's primary key
    email = db.Column(db.String(100), unique=True)  # making it so emails should be unique, no user should share an email
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    notes = db.relationship('Note')
    