from flask import Flask, render_template, flash, request, jsonify, json
import json
from urllib.parse import quote
from numpy import *
from chat import chat
import urllib.request
import json
from urllib.parse import quote
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/')
@cross_origin(supports_credentials=True)
def home():
    return render_template('index.html')

@app.route('/postmethod', methods = ['GET', 'POST'])
@cross_origin(supports_credentials=True)
def getPost():
    
    getPost.jsdata = request.get_json('javascriptData') ### get_json not get form 
    
    return jsonify(getPost.jsdata)
    
@app.route('/getpythondata', methods = ['GET', 'POST'])
@cross_origin(supports_credentials=True)
def pyData():
    
    sentence = getPost.jsdata
    chat(sentence)
    if chat.prob.item() > 0.75:
        return json.dumps(chat.answerBot)
    else:
        return json.dumps('no idea')

if __name__ == '__main__':
    app.run(debug = True)
   


