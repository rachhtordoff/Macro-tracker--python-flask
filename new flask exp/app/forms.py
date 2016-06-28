from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField, SubmitField, RadioField
from wtforms.validators import Required

class calculator(Form):
	weight = IntegerField('weight (kg):')
	height = IntegerField('height (cm):')
	age = IntegerField('age:')
	activity = RadioField('activity level', choices = [('value','Sedentary'),('value_two','Lightly Active'),('value_three','Moderately Active'),('value_four','Very Active'),('value_five','Extremely Active')])
	goal = RadioField('goal', choices = [('value','fat loss'),('value_two','weight gain'),('value_three','Maintenance')])
	certification = RadioField('certification')
	submit = SubmitField('Submit')
	gender = RadioField('Gender', choices = [('value','Female'),('value_two','Male')])
	
class macro_calc(Form) :
	ratio = RadioField('ratio', choices = [('value','30/30/40')])
	submit = SubmitField('Submit')