from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!"

@app.route("/webpage")
def webpage():
    return "Hello guys!! It's my first flask web page 2"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/name")
def name():
    name="Akshra"
    return render_template('new.html',name=name)

app.run(debug=True)
