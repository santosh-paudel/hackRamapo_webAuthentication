from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from forms import loginForm

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
    #this is a temporary list. we will replace this with wtforms template in later versions
    colorHex = ['#ff4444','#FF8800','#33b5e5',
              '#00C851','#9933CC','#ffeb3b',
              '#4285F4','#e91e63 ','#2BBBAD']
    colorName = ['red', 'orange', 'blue',
                 'green', 'puple', 'yellow',
                 'darkBlue', 'pink', 'aqua']
    colors = zip(colorHex, colorName);
    form = loginForm(request.form);

    if request.method == "POST" and form.validate_on_submit():
        print(request.get_data());
        print(form.email.data)
        return "success"

    return render_template('login.html', form=form, colors=colors);

if __name__=='__main__':
    app.run()