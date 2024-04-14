from flask import Flask
app = Flask(__name__)

#Pythonn Decorators

@app.route("/")
def hello_word():
    return "Hello, World!"

if __name__ == '__main__':  
   app.run()