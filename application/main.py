from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from forms import loginForm, colors
from flask_pymongo import PyMongo
app=Flask(__name__)

#debug mode
app.config['DEBUG'] = True

app.secret_key='santosh'
Bootstrap(app)

mongo = PyMongo(app);

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm();
    if request.method == "POST" and form.validate_on_submit():
        print(form.email.data)
        print(form.color.data)
        return redirect(url_for('profile'))

    return render_template('login.html', form=form, colors=colors);

@app.route('/profile')
def profile():
    return "successful"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = loginForm();
    return render_template('register.html', form=form, colors=colors);

if __name__=='__main__':
    app.run()