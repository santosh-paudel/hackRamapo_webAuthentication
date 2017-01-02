import datetime
from app import db

class UserSchema(db.Document):
	email = db.EmailField(unique=True)
	password = db.StringField(default=True)
	active = db.BooleanField(default=True)
	timestamp = db.DateTimeField(default=datetime.datetime.now())