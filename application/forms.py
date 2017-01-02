from flask_wtf import FlaskForm
from wtforms import widgets, StringField, HiddenField
from wtforms import validators, ValidationError
from wtforms.fields.html5 import EmailField


colorHex = ['#ff4444','#ff8800','#33b5e5',
              '#00c851','#9933cc','#ffeb3b',
              '#4285f4','#e91e63','#2bbbad']

colorName = ['red', 'orange', 'blue',
            'green', 'purple', 'yellow',
            'darkBlue', 'pink', 'aqua']

colors = dict(zip(colorHex, colorName));
class loginForm(FlaskForm):
	#validate the hidden field
	#check if the color values received from the client is in the list
	def hidden_form_validation(form,field):
		inputs=loginForm.hash_colors(field.data)
		#print(inputs)
		if len(inputs)!=3:
			raise ValidationError(str(len(inputs))+" color(s chosen. Choose 3")

		for items in inputs:
			if str(items) not in colorHex:
				raise ValidationError("Unauthorized access attempted ", items)

		#print(colorHex)
        
	def hash_colors(data):
		#convert all incoming rgb colors to their hex values
		temp=list(data.split(','))
		temp=list(map(lambda x: '0'+hex(int(x.strip()))[2:] if len(hex(int(x.strip()))[2:])==1 else hex(int(x.strip()))[2:],temp))
		#print(temp)
		inputs=[]
		for items in range(0,len(temp),3):
			cols='#'
			for i in range(3):
				cols+=temp[i+items]
			inputs.append(cols)

		return inputs

	email=StringField('Email', [validators.DataRequired(), validators.Email()])
	color=HiddenField('First box',[validators.DataRequired(), hidden_form_validation])
    