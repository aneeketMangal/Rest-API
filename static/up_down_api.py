from flask import Flask, render_template, request
import requests, json
import pandas as pd
from pytrends.request import TrendReq
import random

app = Flask(__name__)
@app.route('/', methods = ['GET'])
def home():
    return <h1>UpDown</h1>
        
@app.route('/get', methods = ['GET'])   

pytrends = TrendReq(hl='en-US', tz=360)

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