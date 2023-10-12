from flask import Flask, request, render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = 'secret-key'

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(100))

  def __init__(self, email, password, name):
    self.name = name
    self.email = email
    self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

  def checkPassword(self, password):
    return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
  
with app.app_context():
  db.create_all()

@app.route('/')

def index():
  return 'hi'

@app.route('/register', methods=["POST", "GET"])

def register():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    new_user = User(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/login')

  return render_template('register.html')


@app.route('/login', methods=["POST", "GET"])

@app.route('/login',methods=['GET','POST'])

def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        
        if user and user.checkPassword(password):
            session['email'] = user.email
            return redirect('/dashboard')
        else:
            return render_template('login.html',error='Invalid user')

    return render_template('login.html')

@app.route('/dashboard')

def dashboard():
  if session['email']:
    user = User.query.filter_by(email=session['email']).first()
    return render_template('dashboard.html', user=user)
  return 'invalid page'

@app.route('/logout')

def logout():
   session.pop('email', None)
   return redirect('/login')

if __name__ == '__main__':
  app.run(debug=True)