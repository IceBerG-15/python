from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, ValidationError
from wtforms.validators import DataRequired,InputRequired
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = 'It is my secret key, Dont see!'
bootstrap = Bootstrap5(app)

def length_check(form,field):
    if len(field.data)<8:
        raise ValidationError('Password must be atleast 8 characters')
    
def email_check(form,field):
    if '@' not in field.data:
        raise ValidationError('Email must contain @')

class MyForm(FlaskForm):
    email = StringField('email' , validators=[InputRequired(),email_check])
    password = PasswordField('password' , validators=[InputRequired(),length_check])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        e = form.email.data
        p = form.password.data
        if e == 'admin@email.com' and p == '12345678':
            return render_template('success.html')
        return render_template('denied.html')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
