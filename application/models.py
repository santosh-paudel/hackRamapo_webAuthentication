import datetime
from app import db

class UserSchema(db.Document):
    name = db.StringField(unique=False)
    email = db.EmailField(unique=True)
    email_conf = db.BooleanField(default=False)
    password = db.StringField(default=True)
    active = db.BooleanField(default=True)
    timestamp = db.DateTimeField(default=datetime.datetime.now())