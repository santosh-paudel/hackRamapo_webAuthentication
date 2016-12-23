from flask_wtf import FlaskForm
from wtforms import widgets
from wtforms import StringField, SelectMultipleField
from wtforms.validators import DataRequired

class loginForm(FlaskForm):
	data = [(1,'#ff0000'), (2,'#d3ffce'), (3,'#ff7373'),(4,'#ffa500'),(5,'#003366'),(6,'#800080'),(7,'#00800'),(8,'#0099cc'),(9,'#ff4444')]
	username=StringField('Please Enter Your Username',validators=[DataRequired()])
	#for some reason, it's not working
	#we will fix this in later versions. For now,we'll use bootstrap form
	#select_colors = SelectMultipleField('Pick color!',choices=data,option_widget=widgets.CheckboxInput(),widget=widgets.ListWidget(prefix_label=False))