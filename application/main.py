import os
from flask import current_app, render_template, abort, request, flash, redirect, url_for, jsonify
from forms import loginForm, colors
from app import login_manager, flask_bcrypt, app
from flask_login import (current_user, login_required, login_user, logout_user, confirm_login, fresh_login_required)

from libs.User import User

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm();
    if request.method == "POST" and form.validate_on_submit():
        email = request.form.get('email').lower()
        
        userLog = User()
        user = userLog.get_user_with_email(email)
        
        if user and userLog.check_password(form.color.data) and user.is_active:
            #remember = request.form.get("remember", False) == True
            login_user(user)
            print("logged in");
            return redirect('/profile')

        return redirect(url_for('login'))

    return render_template('login.html', form=form, colors=colors);

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'));

@app.route('/profile', methods=['GET','POST'])
def profile():
    if request.method=='POST':
        user_location=request.form
        for i in user_location:
            print(i)
    return render_template('profile.html')

@app.route('/location', methods=['GET','POST'])
def location():
    user_location=request.form
    print('country:',user_location['country'],'city ', user_location['city'])
    return jsonify({'country':user_location['country'],'city':user_location['city']})

    return jsonify({'planet':'Unknown Planet'})
        
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = loginForm();
    if request.method == "POST" and form.validate_on_submit():
        
        #name = form.name.data
        email = request.form.get('email').lower()
        password = request.form.get('color')
        
        user = User(email, password)
        print(user)
        
        try:
            user.save() 
            if login_user(user):
                print("loggedin!")
                return redirect('/')
            else:
                flash("unable to log in")
        except:
            print("Registration Failed")
            
    return render_template('register.html', form=form, colors=colors);

@login_manager.unauthorized_handler
def unauthorized_callback():
	return redirect('/login')

@login_manager.user_loader
def load_user(id):
	if id is None:
		redirect('/login')
	user = User()
	user.get_user_id(id)
	if user.is_active:
		return user
	else:
		return None


if __name__=='__main__':
    app.run()