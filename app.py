from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from text_on_LCD import LCD
from time import sleep

app = Flask(__name__)

try:
    print ('Display will be starting ... ')
    myLcd = LCD()
    print ('Display should be ON ... ')
except:
    print("Could not init LCD!")

@app.route('/status/<status>')

def status_message(status):
    print ("Status: " + status)
    if status == "busy":
        myLcd.setLoop(False)
        sleep(1)
        myLcd.setLoop(True)
        myLcd.busy()
    elif status == "offline":
        myLcd.setLoop(False)
        sleep(1)
        myLcd.destroy()
    elif status == "presenting":
        myLcd.setLoop(False)
        sleep(1)
        myLcd.setLoop(True)
        myLcd.presenting()
    else:
        print("probably available!")
        myLcd.setLoop(False)
        sleep(1)
        myLcd.setLoop(True)
        myLcd.available()       
    return render_template('index.html', value = status)
