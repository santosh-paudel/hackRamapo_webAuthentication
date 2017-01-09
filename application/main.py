import os
from flask import current_app, render_template, abort, request, flash, redirect, url_for, jsonify
from forms import loginForm, registerForm, emailForm, passwordForm, colors
from config import ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD
from flask_login import (current_user, login_required, login_user, logout_user, confirm_login, fresh_login_required)
from util.security import ts
from flask_mail import Message
from app import login_manager, flask_bcrypt, app, mail

from libs.User import User

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    email_form = emailForm()
    if form.validate_on_submit():
        email = request.form.get('email').lower()
        
        userLog = User()
        user = userLog.get_user_with_email(email)
        
        if user and userLog.check_password(form.color.data) and user.is_active:
            login_user(user, remember=True)
            print("logged in");
            return redirect('/profile')

        return redirect(url_for('login'))

    return render_template('login.html', form=form, email_form=email_form, colors=colors);

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
        
@app.route('/reset', methods=['GET', 'POST'])
def reset():
    
    print(request.json['email'])
    email = request.json['email'].lower()

    user = User()
    user.get_user_with_email(email)

    if user:
        subject = "Password Reset Requested"
        token = ts.dumps(email, salt='recover-password')

        recover_url = url_for(
        'reset_password',
        token=token,
        _external=True)

        html = render_template(
            'email/recover.html',
            recover_url=recover_url)

        emails=[]
        emails.append(email)

        msg = Message(subject, sender=ADMINS[0], recipients=emails)
        msg.html = html

        with app.app_context():
            mail.send(msg)
            return 'success'
    return 'error'
        
@app.route('/reset/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        email = ts.loads(token, salt='recover-password', max_age=86400)
    except:
        abort(404)
        
    form=passwordForm()
    
    if form.validate_on_submit():
        user = User()
        
        if user.get_user_with_email(email):
            user.reset_password()
            login_user(user, remember=True)
            return redirect('/profile')
        
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = registerForm();
    if form.validate_on_submit():
        
        name = request.form.get('name')
        email = request.form.get('email').lower()
        password = request.form.get('color')
        
        user = User(email, password, name)
        
        # send email to confirm email
        subject = "Confirm your email for //hackRamapo"

        token = ts.dumps(email, salt='email-confirm-key')

        confirm_url = url_for(
            'confirm_email',
            token=token,
            _external=True)

        html = render_template('email/activate.html',
                              confirm_url=confirm_url)

        emails = []
        emails.append(email)
        
        msg = Message(subject, sender=ADMINS[0], recipients=emails)
        msg.html = html
        
        try:
            user.save()
            if login_user(user, remember=False):
                with app.app_context():
                    mail.send(msg)
                return redirect('/profile')
            else:
                flash("unable to log in")
        except:
            print("Registration Failed")
            
    return render_template('register.html', form=form, colors=colors);

@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = ts.loads(token, salt="email-confirm-key", max_age=86400)
    except:
        abort(404)

    user = User()
    if user.get_user_with_email(email):
        user.email_confirmed()
        login_user(user, remember=True)
        return redirect('/profile')
        
    return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

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