#!/usr/bin/env python
# coding: utf-8
from flask import Flask, redirect, url_for, request
from flask_cors import CORS
import json
import pandas as pd

def createNoteFileIfNotExist():
    f = open("notes.json","a+")
    f.close()

app = Flask(__name__)
CORS(app)

@app.route('/addNotes/<string:keyword>/<string:noteFromUI>',methods=['GET'])
def addNotes(keyword,noteFromUI):
    createNoteFileIfNotExist()
    f = open("notes.json","r")
    data = f.readlines()
    if (len(data) == 0):
        tempDict = {}
        tempDict["key"] = keyword
        tempList = []
        tempList.append(noteFromUI)
        tempDict["note"] = tempList
        data = [tempDict]
        t2={}
        t2["notes"] = data
        js = pd.DataFrame(t2)
        js.to_json("notes.json")
    f.close()

    js = pd.read_json('notes.json')
    i = 0
    flag = 0
    for i in range(len(js["notes"])):
        print("here")
        if (js["notes"][i]["key"] == keyword):
            js["notes"][i]["note"].append(noteFromUI)
            flag = 1
        i = i + 1
    print(flag)
    if flag == 0:
        print("there")
        tempMainList = []
        tempDict = {}
        tempDict["key"] = keyword
        tempList = []
        tempList.append(noteFromUI)
        tempDict["note"] = tempList
        tempMainList.append(tempDict)
        js.loc[i] = tempMainList
        print(js)
        js.to_json("notes.json")

    js.to_json("notes.json")
    return("success")


@app.route('/showNotes/<string:keyword>')
def showNote(keyword):
    createNoteFileIfNotExist()
    f = open("notes.json","r")
    data = f.read()
    if len(data) == 0:
        return "Null"
    jsonData = json.loads(data)
    f.close()
    i = 0
    for i in range(len(jsonData['notes'])):
        print(jsonData['notes'][str(i)]['key'])
        if (jsonData['notes'][str(i)]['key']) == keyword:
            return (jsonData['notes'][str(i)])
        i = i + 1
    return "Null"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5150',debug=True)
