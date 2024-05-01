from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField


app = Flask(__name__)
app.secret_key = "021003241217_The_Best_Number_Combination"

class LoginField(FlaskForm):
    email = StringField("Email")
    password = StringField("Password")


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    login_form = LoginField()
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
