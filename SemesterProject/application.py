from flask import Flask, render_template, url_for
from flask.logging import create_logger
import logging 

# logging level is set to DEBUG
# %(asctime)s— The timestamp as a string. %(levelname)s—The logging level as a string.
# %(name)s—The logger name as a string. %(threadname)s—The thread name as a string.
# %(message)s—The log message.
logging.basicConfig(level = logging.DEBUG, format = f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)

log = create_logger(app)

@app.route('/')
def index():
    log.debug('this is a DEBUG message ')
    log.info('this is an INFO message ')
    log.warning('this is a WARNING message ')
    log.error('this is an ERROR message ')
    log.critical('this is a CRITICAL message ')
    return render_template("index.html")

@app.route('/index/home')
def home():
    return render_template("home.html")

@app.route('/index/home/about_me')
def about_me():
    return render_template("about_me.html")

@app.route('/index/home/travel')
def travel():
    return render_template("travel.html")

@app.route('/index/home/cv')
def cv():
    return render_template("cv.html")

@app.route('/index/home/contact_info')
def contact_info():
    return render_template("contact_info.html")

Hello = hello
