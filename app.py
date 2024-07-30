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

@app.route('/home',methods=['GET','POST'])
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='GET':
      try:
        email=login_session['user']['email']
      except:
        email='Guest'
      return render_template('home.html',email = email)
    booksOwned=db.child('carts').child(login_session['user']['localId']).child('book').get().val()
    db.child('carts').child(login_session['user']['localId']).child('book').set(booksOwned+1)
    return redirect(url_for('home'))
        



@app.route('/signIn',methods=['GET','POST'])
def signIn():
    if request.method == 'GET':
        return render_template('signIn.html')
    else:
        email = request.form['email']
        password = request.form['password']
        login_session['quotes'] = []
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email,password)
        except Exception as e:
            print("Error:",e)
        return redirect(url_for('home'))
    
@app.route('/signUp',methods=['GET','POST'])
def signUp():
    if request.method == 'GET':
        return render_template('signUp.html')
    email = request.form['email']
    password = request.form['password']
    login_session['quotes'] = []
    try:
        login_session['user'] = auth.create_user_with_email_and_password(email,password)
        print(login_session['user']['localId'])
        db.child('carts').child(login_session['user']['localId']).set({"book":0})
    except Exception as e:
        print("Error:",e)

    return redirect(url_for('home'))


@app.route('/signOut')
def signOut():
    auth.current_user = None
    login_session['user']=None
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)