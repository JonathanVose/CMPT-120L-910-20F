from flask import Flask, render_template, url_for
from flask.logging import create_logger
import logging 

# logging level is set to DEBUG
# %(asctime)s— The timestamp as a string. %(levelname)s—The logging level as a string.
# %(name)s—The logger name as a string. %(threadname)s—The thread name as a string.
# %(message)s—The log message.
logging.basicConfig(level = logging.DEBUG, format = f'%(asctime)s %(levelname)s : %(message)s')

app = Flask(__name__)

log = create_logger(app)

@app.route('/')
def index():
    log.debug('this is a DEBUG message ')
    log.info('this is an INFO message ')
    log.warning('this is a WARNING message ')
    log.error('this is an ERROR message ')
    log.critical('this is a CRITICAL message ')
    log.info('the user traveled to the index page')
    return render_template("index.html")

@app.route('/index/home')
def home():
    log.info('the user traveled to the home page')
    return render_template("home.html")

@app.route('/index/home/about_me')
def about_me():
    log.info('the user traveled to the about_me page')
    return render_template("about_me.html")

@app.route('/index/home/travel')
def travel():
    log.info('the user traveled to the travel page')
    log.warning('the travel page is not done')
    return render_template("travel.html")

@app.route('/index/home/cv')
def cv():
    log.info('the user traveled to the cv page')
    log.warning('the cv page is not done')
    return render_template("cv.html")

@app.route('/index/home/contact_info')
def contact_info():
    log.info('the user traveled to the contact_info page')
    log.warning('the contact_info page is not done')
    return render_template("contact_info.html")


