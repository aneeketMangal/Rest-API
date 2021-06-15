from flask import Flask, render_template, request, jsonify, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from forms.login_form import LoginForm
from forms.register_form import RegisterForm
from flask.views import MethodView

app = Flask(__name__)
app.config['SECRET_KEY'] = '9616543127'

app.config["MONGO_URI"] = "mongodb://localhost:27017/todo_db"
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
    {
        'user': 'Aneeket Mangal', 
        'userImage': "https://avatars.githubusercontent.com/u/54039514?v=4",
        'content': 'Champions Never die.',
        'date': '24.09.01'
        # 'image': 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg'
    },
    {
        'user': 'Aneeket Mangal', 
        'userImage': "https://avatars.githubusercontent.com/u/54039514?v=4",
        'content': 'Champions Never die.',
        'date': '24.09.01'
        # 'image': 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg'
    },
    
]

@app.route("/addpost")
def addpost():
    print("sdf")
    # try:
    db.todos.insert_one({'title': "todo title", 'body': "todo body"})
    # except:
    #     print("not happpening")
    return jsonify(message="success")





@app.route('/')
@app.route('/home')
def home():
    print("home")
    return render_template('index.html', posts = posts)

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if(form.validate_on_submit()):
        flash(f'Account created successfully {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)

@app.route("/action/update-text")
def update_text():
    posts[0]['user'] = "sdfjsifd"
    print("fdsa")
    return jsonify({'success':1})




if __name__ == '__main__':
    app.run(debug = True)