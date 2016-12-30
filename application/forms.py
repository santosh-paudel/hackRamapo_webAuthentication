from flask_wtf import FlaskForm
from wtforms import widgets, StringField, SelectMultipleField
from wtforms import validators, ValidationError
from wtforms.fields.html5 import EmailField

COLOR_CHOICES = [('1','#ff4444'),('2','#FF8800'),('3','#33b5e5'),('4','#00C851'),('5','#9933CC'),('6','#ffeb3b'),('7','#4285F4'),('8','#e91e63'),('9','#2BBBAD')]

class loginForm(FlaskForm):
    color=SelectMultipleField('Colors', choices=COLOR_CHOICES)
    email=StringField('Email', [validators.DataRequired(), validators.Email()])