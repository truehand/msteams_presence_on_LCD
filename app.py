from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from text_on_LCD import LCD
from time import sleep

app = Flask(__name__)

recentStatus = "offline"

try:
    print ('Display will be starting ... ')
    myLcd = LCD()
    print ('Display should be ON ... ')
except:
    print("Could not init LCD!")

@app.route('/status/<status>')

def status_message(status):
    print ("Status: " + status)
    if status == "busy" and recentStatus != "busy":
        recentStatus = "busy"
        myLcd.setLoop(False)
        sleep(2)
        myLcd.setLoop(True)
        myLcd.busy()
    elif status == "offline" and recentStatus != "offline":
        recentStatus = "offline"
        myLcd.setLoop(False)
        sleep(2)
        myLcd.destroy()
        myLcd.setLoop(True)
    elif status == "presenting" and recentStatus != "presenting":
        recentStatus = "presenting"
        myLcd.setLoop(False)
        sleep(2)
        myLcd.setLoop(True)
        myLcd.presenting()
    elif status == "available" and recentStatus != "available":
        recentStatus = "available"
        print("probably available!")
        myLcd.setLoop(False)
        sleep(2)
        myLcd.setLoop(True)
        myLcd.available()       
    #return render_template('index.html', value = status)
    return "200 OK"
