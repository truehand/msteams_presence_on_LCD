from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from LCD import LCD
from time import sleep

recentStatus = "unknown"

try:
    print ('Display will be starting ... ')
    myLcd = LCD()
    print ('Display should be ON ... ')
except:
    print("Could not init LCD!")

app = Flask(__name__)

def task(status):
    global recentStatus
    print("Task acting on " + status)
    sleepTime = 3
    if status == "offline" and recentStatus != "offline":
        recentStatus = "offline"
        myLcd.setLoop(False)
        sleep(sleepTime)
        myLcd.setLoop(True)
        myLcd.offline()
    elif status.startswith("present") and recentStatus != "presenting_act":
        recentStatus = "presenting_act"
        myLcd.setLoop(False)
        sleep(sleepTime)
        myLcd.setLoop(True)
        myLcd.presenting()
    elif status.startswith("dnd") and recentStatus != "dnd":
        recentStatus = "dnd"
        myLcd.setLoop(False)
        sleep(sleepTime)
        myLcd.setLoop(True)
        myLcd.dnd()
    elif status.startswith("inacall") and recentStatus != "inacall":
        recentStatus = "inacall"
        myLcd.setLoop(False)
        sleep(sleepTime)
        myLcd.setLoop(True)
        myLcd.inAcall()
    elif status.startswith("away") and recentStatus != "away":
        recentStatus = "away"
        myLcd.setLoop(False)
        sleep(sleepTime)
        myLcd.setLoop(True)
        myLcd.away()    
    elif status.startswith("brb") and recentStatus != "brb":
        recentStatus = "brb"
        myLcd.setLoop(False)
        sleep(sleepTime)
        myLcd.setLoop(True)
        myLcd.brb()        
    ## do we have any other special messages? that we want to display?
    elif status.startswith("msg:") and recentStatus != "msg":
        recentStatus = "msg"
        myLcd.setLoop(False)
        sleep(sleepTime)
        myLcd.setLoop(True)
        myLcd.msg(status[4:], True)
    elif status.startswith("available") and recentStatus != "available":
        recentStatus = "available"
        myLcd.setLoop(False)
        sleep(sleepTime)
        myLcd.setLoop(True)
        myLcd.available()
    elif status.startswith("busy") and recentStatus != "busy":
        recentStatus = "busy"
        myLcd.setLoop(False)
        sleep(sleepTime)
        myLcd.setLoop(True)
        myLcd.busy()
    return recentStatus
 
@app.route('/status/<string:status>')
def status_message(status):
    print ("Received activity: " + status)
    return task(status), 200

@app.route('/')
def get_status():
    global recentStatus
    return render_template('index.html', teamsPresence=recentStatus, lcdStatus=str(myLcd.getLcdStatus())), 200

@app.route('/off')
def off():
    myLcd.destroy()
    return "0",200

@app.route('/on')
def on():
    myLcd.lightOn()
    return "1", 200