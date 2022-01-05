from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import redis
from rq import Queue

from LCD import LCD
from time import sleep

recentStatus = "unknown"

try:
    print ('Display will be starting ... ')
    myLcd = LCD()
    print ('Display should be ON ... ')
except:
    print("Could not init LCD!")

r = redis.Redis()
q = Queue(connection=r)
app = Flask(__name__)

def bg_task(status):
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
        myLcd.msg(status[4:])
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
    task = q.enqueue(bg_task, status)
    print (f"Task ({job.id}) added to queue at {job.enqueued_at}")
    jobs = q.jobs  # Get a list of jobs in the queue
    q_len = len(q)  # Get the queue length

    message = f"Task queued at {task.enqueued_at.strftime('%a, %d %b %Y %H:%M:%S')}. {q_len} jobs queued"

    return message, 200

@app.route('/')
def get_status():
    global recentStatus
    print (q.jobs[-1])
    return render_template('index.html', teamsPresence=recentStatus, lcdStatus=str(myLcd.getLcdStatus())), 200

@app.route('/off')
def off():
    myLcd.destroy()
    return "0",200

@app.route('/on')
def on():
    myLcd.lightOn()
    return "1", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)