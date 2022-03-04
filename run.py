from flask import Flask, render_template, flash, request, jsonify, json
import json, requests,  sqlite3, random
from datetime import datetime
from urllib.parse import quote
from numpy import *
from chat import chat
from urllib.parse import quote
from flask_cors import CORS, cross_origin




arrayOfWrongChoices = ["Might need to rephrase that", "Hey I know the answer to this! 42304... No ?", "Try asking something else", "How about NO"]

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
    print(sentence)
    date = datetime.today().strftime('%Y-%m-%d %H:%M:')
    if chat.prob.item() > 0.75:
        con = sqlite3.connect('ChatBot.db')
        cur = con.cursor()
        cur.execute("insert into Chatbot values(?,?,?)",(date, sentence, 'T')) 
        con.commit()
        con.close()
        return json.dumps(chat.answerBot)
        
    else:
        url = requests.get(f'https://api.duckduckgo.com/?q={sentence}&format=json&pretty=1')
        text = url.text
        y = json.loads(text)
        try:
            if (y["Abstract"] == ""):
                con = sqlite3.connect('ChatBot.db')
                cur = con.cursor()
                cur.execute("insert into Chatbot values(?,?,?)",(date, sentence, 'F')) 
                con.commit()
                con.close()
                return json.dumps("duckduckGo says: "+y["RelatedTopics"][0]["Text"])
            else:
                con = sqlite3.connect('ChatBot.db')
                cur = con.cursor()
                cur.execute("insert into Chatbot values(?,?,?)",(date, sentence, 'F')) 
                con.commit()
                con.close()
                con.commit()
                con.close()
                return json.dumps("duckduckGo says: "+y["Abstract"])
        
        except IndexError:
            return json.dumps(random.choice(arrayOfWrongChoices))
            

        

if __name__ == '__main__':
    app.run(debug = True)
   







    
    