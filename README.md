# msteams_presence_on_LCD

Diplays your Microsoft Teams presence on a mini LCD screen connected to a Raspbery Pi.

![alt-text](https://github.com/truehand/msteams_presence_on_LCD/blob/main/static/lcd1.jpg?raw=true "A busy status displayed on the LCD")

Currently, I use it in conjunction with PresenceLight (https://github.com/isaacrlevin/PresenceLight) which reads your Teams status (available/away/presenting etc). Alternatively, it can be integrated with any custom RESTful "Microsoft Graph API" applications that can read and report your Teams status / presence information, as it is already possible to read Teams presence through this MS Graph API: 

https://docs.microsoft.com/en-us/graph/api/presence-get?view=graph-rest-1.0&tabs=http

For example, a GET request made to https://graph.microsoft.com/v1.0/me/presence will give you a response similar to this:

{  
   "id": "fa8bf3dc-eca7-46b7-bad1-db199b62afc3",  
   	"availability": "Available",  
   	"activity": "Available"  
}  

If you prefer to use the Microsoft Graph API directly as above, you need to set up an Azure AD application and get its client ID as well as the created secret value. These fields are sent in the header of the above request. Your Azure AD app must have these permissions:

* Presence.Read
* User.Read

Either way (by using PresenceLight which in turn uses the Microsoft Graph API) or by using the Microsotft Graph API directly yourselves, you can obtain your status/presence information.

Then use this Flask app to display the message on a generic mini LCD connected to a Raspbery Pi:

First, set Flask app environment variable:

*export FLASK_APP=presence_server.py*

Then run it with: 

*flask run --host=0.0.0.0 -p 5000*

Or, simply use the provided run.sh

(Here, 0.0.0.0 means reachable by any IP on the network, and 5000 is the port)

The code that runs Microsoft Graph API to obtain your Teams status may be running on the same Raspbery Pi, or somewhere else. If it's running on a laptop, as an example, and if your Raspbery Pi's IP address is 192.168.68.27 on the same network, you can change your LCD display to reflect your status info from your laptop by these simple GET requests:

- http://192.168.68.127:5000/status/available

- http://192.168.68.127:5000/status/busy

- http://192.168.68.127:5000/status/presenting_act

and so on.

Other supported status messages to display are in the app.py. Yo ucan always switch off the LCD screen by:

http://192.168.68.127:5000/off

As these generic LCD screens usually have two lines each of which is 16 characters long, I am displaying the current time on the second line which is being updated every second.

Any problems/clarifications just ask.