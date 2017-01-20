import os
from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail

app=Flask(__name__)

app.config['TEMPLATE_AUTORELOAD']=True

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

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'hackRamapo@gmail.com'
app.config['MAIL_PASSWORD'] = 'hackRamapo123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['ADMINS'] = ['hackRamapo@gmail.com']

# sending email
mail = Mail(app)