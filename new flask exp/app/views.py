from app import app
from flask import Flask, render_template, flash, redirect, request, session, url_for
from .forms import calculator, macro_calc


def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1

@app.route('/homepage', methods=['GET', 'POST'])
def login():
#if form.validate_on_submit():
	
	if request.method == 'GET':
		form = calculator()
		return render_template('homepage.html', form=form, output=-1, message_error = None)
		
	if request.method == 'POST':
		output = None
		sumSessionCounter()
		form = calculator(request.form) # this pulls inputed data from the form
		valid, error = validate_calc(form) # validates the form and stores any error messages
		if valid == True: #if the validation method passes then...
			weight = form.weight.data
			height = form.height.data
			age = form.age.data
			activity = form.activity.data
			goal = form.goal.data
			gender = form.gender.data
			output = calculate_TDEE(weight, height, age, gender, activity)
			final, info = calculate_goal(goal, output)
			session['counter'] = (final)
		return render_template('index.html', form=form, output=output, message_error=error, goals=final, info=info, session=session)	
		#render the homepage again and pass the output and any error messages from the validation method

@app.route('/clear')
def clearsession():
    # Clear the session
    session.clear()
    # Redirect the user to the main page
    return redirect(url_for('login'))
		
@app.route('/macro', methods=['GET', 'POST'])
def macros():

	if request.method == 'GET':
		form = macro_calc()
		return render_template('macro.html', form=form)
		
	if request.method == 'POST':
		sumSessionCounter()
		form = macro_calc(request.form)
		ratio = form.ratio.data
		ratio_fat = calculate_fat(ratio, session['counter'])
		ratio_carb = calculate_carb(ratio, session['counter'])
		ratio_protein = calculate_protein(ratio, session['counter'])
	return render_template('macroratio.html', form=form, ratio_fat=ratio_fat, ratio_carb=ratio_carb, ratio_protein=ratio_protein)	
		
def calculate_TDEE(weight, height, age, gender, activity): 
	""" This calculates and returns Total daily expenditure """
	if gender == 'value':
		weight_input = (weight * 9.6) + 655
		height_input = (height * 1.8)
		age_input = (age * 4.7)
	else:
		weight_input = (weight * 13.7) + 66
		height_input = (height * 5)
		age_input = (age * 6.8)
	

	bmr = weight_input + height_input - age_input
	final = 0
	
	if activity == 'value':
		final = bmr * 1.2
 
	elif activity == 'value_two':
		final = bmr * 1.375
 
	elif activity == 'value_three':
		final = bmr * 1.55
 
	elif activity ==  'value_four':
		final = bmr * 1.725
  
	elif activity == 'value_five':
		final = bmr * 1.9
		
	
	return final
	
def validate_calc(form_validation):
	""" This checks that inputs have been entered into the form """
	if form_validation.weight.data == None:
		return False, "please input weight"
	if form_validation.height.data == None:
		return False, "please input height"	
	if form_validation.age.data == None:
		return False, "please input age"
	if form_validation.activity.data == None:
		return False, "please input activity"
	if form_validation.goal.data == None:
		return False, "please input goal"
	if form_validation.gender.data == None:
		return False, "please input gender"		
	return True, ""

def calculate_goal(goal_input, tdee):
	""" This calculates the TDEE based on the users goal input """
	global final_calories
	if goal_input == 'value':
		final_calories = tdee - 500, "for 1lb fat loss per week"
	elif goal_input == 'value_two':
		final_calories = tdee + 500, "for 1lb weight gain per week"
	else:
		final_calories = tdee, "for maintenance "
	return final_calories
	
def calculate_fat(ratio, Session):
	""" This will calculate macronutrients based on calorie intake """
	if ratio == 'value':
		fat = (Session * 0.3)/9
		return fat
	return "Please select a ratio"
	
def calculate_carb(ratio, Session):
	if ratio == 'value':
		protein = (Session * 0.3)/4
		return protein
	return "Please select a ratio"
	
def calculate_protein(ratio, Session):
	if ratio == 'value':
		carbs = (Session * 0.4)/4
		return carbs
	return "Please select a ratio"