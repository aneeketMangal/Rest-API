from flask import Flask, render_template, request, jsonify, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from forms.login_form import LoginForm
from forms.register_form import RegisterForm
from elements.user.user import User
# from flask.views import MethodView

from flask_classful import FlaskView, route
from database.user_database import UserDatabase

app = Flask(__name__)
app.config['SECRET_KEY'] = '9616543127'

app.config["MONGO_URI"] = "mongodb+srv://admin:aneeketissuperman@cluster0.i38f8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
app.config["CURRENT_USER"] = None
app.config["CURRENT_USER_NAME"] = "Anonymous"
app.config["CURRENT_PFP"] = "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg"
app.config["LOGO"] = "https://codesign.com.bd/conversations/content/images/2020/03/Sprint-logo-design-Codesign-agency.png"
app.config["APP_NAME"] = "The Rest Crest"

mongodb_client = PyMongo(app)
db = mongodb_client.db




posts = [
    {
        'user': 'Aneeket Mangal', 
        'userImage': 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg',
        'content': 'We are rolling',
        'date': '24.09.01',
        'image': 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg'
    },
    
    
]*3


@app.route('/')
@app.route('/home')
def home():
    userData = {}
    if(app.config['CURRENT_USER']):
        userData = app.config['CURRENT_USER'].getInfo()
    return render_template('index.html', posts = posts, userData = userData)

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if(form.validate_on_submit()):
        databaseLog = user_db.checkUserAvailability(form.username.data, form.email.data)
        if(databaseLog['isAvailable']):
            user_db.addUser(form.username.data, form.password.data)
            flash(f'Account created successfully {form.username.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash(databaseLog['errorLog'], 'danger')

    return render_template('register.html', title = 'Register', form = form)


@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/login',  methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if(form.validate_on_submit()):
        databaseLog = user_db.verifyUserDetails(form.username.data,form.password.data)
        app.config["CURRENT_USER"] = User(databaseLog['userData'])
        app.config["CURRENT_USER_NAME"] = databaseLog['userData']['username']
        app.config["CURRENT_PFP"] = databaseLog['userData']['pfp']
        temp = app.config["CURRENT_PFP"]
        print(temp)
        
        if(databaseLog['isAvailable']):
            # user_db.addUser(form.username.data, form.password.data)
            flash(f'Welcome {form.username.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash(databaseLog['errorLog'], 'danger')

    return render_template('login.html', title = 'Login', form = form)

@app.route("/database/adduser")
def addUser():
    user_db.test()
    return jsonify({'success':1})




if __name__ == '__main__':
    user_db = UserDatabase(db)
    app.run(debug = True)