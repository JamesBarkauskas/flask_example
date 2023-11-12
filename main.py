# our main python file where we can run our app / start our server from...
# we import our website package and grab the 'create_app' function from __init__.py
from website import create_app  # we can import website folder because we made it a python package with the __init__ file...

app = create_app()

if __name__ == '__main__':  # can only run our app from our main file
    app.run(debug=True)     # we'd turn off debug=True in production...
    
    