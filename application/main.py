from flask import Flask, request, render_template, redirect,url_for
from flask_bootstrap import Bootstrap
from forms import loginForm,colors
app=Flask(__name__)

#debug mode
app.config['DEBUG'] = True

#reload templates automatically
#app.config['TEMPLATES_AUTO_RELOAD'] = True

app.secret_key='santosh'
Bootstrap(app)

@app.route('/')
def home():
    return render_template('layout.html')

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


if __name__=='__main__':
    app.run()