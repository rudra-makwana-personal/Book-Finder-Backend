#!/usr/bin/env python
# coding: utf-8
from flask import Flask, redirect, url_for, request
from flask_cors import CORS
import re
import datetime

app = Flask(__name__)
CORS(app)

def createLogFileIfNotExist():
    f = open("log.txt","a+")
    f.close()

def checkForKeyword(keyword):
    c = 0
    f = open("log.txt","r")
    data = f.readlines()
    for d in data:
        if d.find(keyword) != -1:
            return c
        c = c + 1
    c = -1
    f.close()
    return c

def freqIncrement(c):
    f = open("log.txt","r")
    i = 0
    data = f.readlines()
    for d in data:
        if i == c:
            number = re.findall("\d*$",d)
            if int(number[0])<10:
                tempNumber = int(number[0]) + 1
                d = d[:-2]
                d = d+str(tempNumber)+"\n"
                data[i] = d
            else:
                tempNumber = int(number[0]) + 1
                d = d[:-3]
                d = d + str(tempNumber) + "\n"
                data[i] = d
        i = i + 1
    f.close()
    f=open("log.txt","w")
    f.writelines(data)
    f.close()

@app.route('/log/<string:keywords>')
def logFile(keywords):
    currentDateTime = str(datetime.datetime.today())
    createLogFileIfNotExist()
    c = checkForKeyword(keywords)
    if c>=0:
        freqIncrement(c)
    else:
        data = "keywords: "+keywords+" , lastTimeSearched: "+currentDateTime+" , frequency: "+str(1)
        f = open("log.txt","a+")
        f.write(data)
        f.write("\n")
        f.close()
    return "ok"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5050',debug=True)

