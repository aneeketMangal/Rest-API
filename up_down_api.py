from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
@app.route('/', methods = ['GET'])
def home():
    return render_template('session.html')
currLoggedIn = ""
d = {}
        
@app.route('/get', methods = ['GET'])   
import pandas as pd
from pytrends.request import TrendReq
import random
pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["biryani", "salman", "sachin","byjus", "facebook", "burger", "neet", "jee", "laptop","sony", "tiktok", "pizza", "github", "codechef", "gfg", "lenovo", "cricket", "hockey", "chess", "among us", "vidit gujrathi", "tappu", "yashraj", "vimal", "microsoft","google", "mi", "ipl", "csk", "rcb", "kabaddi", "kutta", "billi"] 


start = random.choice(kw_list)
while(True):
    
    while(True):
        end = random.choice(kw_list)
        if(start != end):
            break
    temp = [start, end]
    print(temp)
    
    pytrends.build_payload(temp, timeframe='2017-01-01 2021-01-01', geo='IN')
    df = pytrends.interest_over_time()
    x = list(df[start].astype(int))
    y = list(df[end].astype(int))
    x = sum(x)
    y = sum(y)
    
    response = int(input())
    start = end
    if(response == 1 and x <=y):
        continue
    elif(response == 0 and x >= y):
        continue
    else:
        print("Wrong!!!")
        break
    
# df.to_csv('file_name.csv')
    # print(dfs.head(50))
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

        d[name].append([user, message])
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
            return {"data":d[name]}
        else:
            return {"error":"no such room"}
        
    else:
        return {"error": "invalid arguements"}


if __name__ == '__main__':
    app.run(debug=True)