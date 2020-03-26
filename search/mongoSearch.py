#!/usr/bin/env python
# coding: utf-8

# In[21]:


from flask import Flask, redirect, url_for, request, jsonify
from flask_cors import CORS
from bson.json_util import dumps
from bson import ObjectId
import pymongo
import json


app = Flask(__name__)
CORS(app)

@app.route('/search/<string:keywords>')
def searchInMongo(keywords):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["cloudAssignment3"]
    text = pymongo.TEXT
    mydb["booksAndAuthors"].create_index([("Author", text),('Book_Name',text)],default_language='english')
    results = mydb["booksAndAuthors"].find({"$text": {"$search": keywords}})
    #print(results)
    newList = []
    data = []
    data.append({"Keyword":keywords})

    for x in results:
        newList.append(x)
        data.append({"Book_Name": x["Book_Name"]})
        data.append({"Author": x["Author"]})

    with open("catalogue.json","a+") as json_file:
    	json.dump(data, json_file, indent=4)

    return dumps(newList)

        
if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5000',debug=True)





