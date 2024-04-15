# Can browse for personal site and portfolio {html5up.net | squarespace.com/templates/browse/online-stores}

# In website console, set "document.body.contentEditable=true"
# Then, CTRL + S the website to get a htm file
# Replace everything in index.html
# Shift + press Refresh Button for hard refresh

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    