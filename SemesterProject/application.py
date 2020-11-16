from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/home/about_me')
def about_me():
    return render_template("about_me.html")

@app.route('/home/travel')
def travel():
    return render_template("travel.html")

@app.route('/home/cv')
def cv():
    return render_template("cv.html")

@app.route('/home/contact_info')
def contact_info():
    return render_template("contact_info.html")

hello = hello 