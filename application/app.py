import os
from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app=Flask(__name__)

# database connection
app.config['MONGODB_SETTINGS'] = {
    'db': 'hackRamapo',
}

app.secret_key='santosh'
Bootstrap(app)

#debug mode
app.debug = os.environ.get('DEBUG', True);

db = MongoEngine(app)   #connect to MongoEngine
app.session_interface = MongoEngineSessionInterface(db) #sessions

# used to salt password
flask_bcrypt=Bcrypt(app)

# associate flask-login with current app
login_manager = LoginManager()
login_manager.init_app(app)