""" Greet someone with welcome 


"""

from flask import Flask, request

app = Flask(__name__)
# /welcome
# Returns “welcome”
# /welcome/home
# Returns “welcome home”
# /welcome/back
# Return “welcome back”

@app.route('/greet/welcome')
def welcome():
    return "welcome"

@app.route('/greet/welcome/home')
def welcome_home():
    return "welcome home"
    
@app.route('/greet/welcome/back')
def welcome_back():
    return "welcome back"


