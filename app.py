from flask import Flask, render_template,request,redirect,url_for
from flask import session as login_session
import pyrebase


firebaseConfig = {
  "apiKey": "AIzaSyDZ4pS2tY95eqtxLsqUCOllfePwBjtOkfE",
  "authDomain": "trash-project-d71b5.firebaseapp.com",
  "projectId": "trash-project-d71b5",
  "storageBucket": "trash-project-d71b5.appspot.com",
  "messagingSenderId": "986872772198",
  "appId": "1:986872772198:web:d03f739984ad4644f55fa7",
  'databaseURL':"https://trash-project-d71b5-default-rtdb.europe-west1.firebasedatabase.app/"
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