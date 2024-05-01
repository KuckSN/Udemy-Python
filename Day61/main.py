from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
app.secret_key = "021003241217_The_Best_Number_Combination"
bootstrap = Bootstrap5(app)

class LoginField(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginField()
    if login_form.validate_on_submit():
        if login_form.email.data=="admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
