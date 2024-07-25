from flask import Flask, render_template,request,redirect,url_for
from flask import session as login_session
import pyrebase
import math
import time
import random
import threading

firebaseConfig = {

}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

app = Flask(__name__)
app.config['SECRET_KEY']="CS forever"

db =firebase.database()

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)