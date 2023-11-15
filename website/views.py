# our views
# most views will go in here, views not related to authentication and routes that users can navigate to
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user    
from .models import Note            # import our note class
from . import db                    # import our database...
import json

# a blueprint simply means that this file, views.py, should contain routes...
views = Blueprint('views', __name__)     # this defines the name of our blueprint and sets up our blueprint for our app (we'll do same in auth.py)


@views.route('/', methods=['GET', 'POST'])   # defining our home page route (this is a decorator),, we then add our http requests so we can send our data to our db
@login_required     # cannot access home page unless you're logged in...
def home():         # whatever is in our home funciton, will run when we go to the '/' route
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id = current_user.id) 
            db.session.add(new_note)        # add the note to our database
            db.session.commit()
            flash('Note added!', category='success')
            
    return render_template("home.html", user=current_user) # pass in 'user = current_user' so that we can detect if someone is logged in

# adding a new route for delete-note.. after we implement our javascript function to delete a note..
@views.route('/delete-note', methods=['POST'])  # 2:10 into video... 
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)   # look for the note with that specific id...
    
    # to delete the object from db.., check if note exists..
    if note:
        if note.user_id == current_user.id:     # if the current note belongs to the current user...
            db.session.delete(note)             # then we can actually delete the note
            db.session.commit()
           
    return jsonify({})                  # return an empty response, bc we have to return something
        
        