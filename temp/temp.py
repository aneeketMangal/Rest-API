from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from database import Database
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///rest_crest.db"
# db = SQLAlchemy(app)

# class Database(db.Model):
    
#     serial = db.Column(db.Integer, primary_key = True)
#     roomName = db.Column(db.String(200), nullable = False)
        
#     def __repr__(self):
#         return f"{self.serial} - {self.roomName}"
    



@app.route('/', methods = ['GET'])
def home():
    todo = Database(roomName = "aneeket")
    db.session.add(todo)
    db.session.commit()
    return render_template('index.html')

d = {}
@app.route('/login/<name>', methods = ['GET'])
def login(name):
    if(request.method == 'GET'):
        if(name in d):
            dd = {"data":d[name]}
            return dd
        
        else:
            d[name] = []
            dd = {"data":d[name]}
            return dd
        
@app.route('/send', methods = ['GET'])   
def send():
    request_data = request.args
    if(request_data):
        name = ''
        message = ''
        user = ''
        if('message' in request_data):
            message = request_data['message']
        if('name' in request_data):
            name = request_data['name']
        else:
            return 'BAD RESPONSE'
        if('user' in request_data):
            user = request_data['user']
        else:
            return 'BAD RESPONSE'

        d[name].append({"user": user, "body":message})
        # print(d[name])
        return {"name": name,"user": user,"message": message, "D":str(d[name])}
        
    else:
        return {"error": "dfosnaopi"}
    
    
@app.route('/recieve', methods = ['GET'])   
def recieve():
    request_data = request.args
    if(request_data):
        name = ''
        if('name' in request_data):
            name = request_data['name']
            print("done")
            return jsonify(d[name])
        else:
            return {"error":"no such room"}
        
    else:
        return {"error": "invalid arguements"}


@app.route('/test', methods = ['GET'])  
def test():
    return jsonify({"test":"test"})
    

if __name__ == '__main__':
    app.run(port=8000, debug=False)