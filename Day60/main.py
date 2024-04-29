from flask import Flask, render_template, request
import requests
import smtplib

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/405ba6ca0d39dc70fa89").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        send_email(data['name'], data['email'], data['phone'], data['message'])
        return render_template('contact.html', msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route("/form-entry", methods=['POST'])
def receive_data():
    data = request.form
    print(data['name'])
    print(data['email'])
    print(data['phone'])
    print(data['message'])
    return "<h1>Successfully sent your message</h1>"

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


def send_email(name, email, phone, message):
    email_message = f"Subject: New message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login("OWN_EMAIL", "OWN_PASSWORD")
        connection.sendemail("OWN EMAIL", "OWN EMAIL", email_message)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
