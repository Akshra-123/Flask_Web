from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!"

@app.route("/webpage")
def webpage():
    return "Hello guys!! It's my first flask web page 2"

app.run(debug=True)
