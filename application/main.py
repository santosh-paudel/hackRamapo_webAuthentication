from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import loginForm


app=Flask(__name__)
app.secret_key='santosh'
Bootstrap(app)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/login',methods=['GET','POST'])
def login():
    #this is a temporary list. we will replace this with wtforms template in later versions
    colors=['#ff0000','#d3ffce','#ff7373','#ffa500','#003366','#800080','#00800','#0099cc','#ff4444']
    form=loginForm()
    if form.validate_on_submit():
        print(form.username.data)
        return "success"

    return render_template('login.html',form=form,colors=colors)

if __name__=='__main__':
    app.run(debug=True)