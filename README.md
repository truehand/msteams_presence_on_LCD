# msteams_presence_on_LCD

Diplays your Microsoft Teams presence on a mini LCD screen.

Currently, I use it in conjunction with PresenceLight (https://github.com/isaacrlevin/PresenceLight) which reads your Teams status (available/away/presenting etc). Alternatively, it can be integrated with any custom RESTful "Microsoft Graph API" applications that can read and report your Teams status / presence information, as it is possible to read Teams presence through this MS Graph API: 

https://docs.microsoft.com/en-us/graph/api/presence-get?view=graph-rest-1.0&tabs=http

A GET request made to https://graph.microsoft.com/v1.0/me/presence will give you a response similar to this:

HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 1574

{  
	"id": "fa8bf3dc-eca7-46b7-bad1-db199b62afc3",
	"availability": "Available",
	"activity": "Available"
}

If you prefer to use this API, you need to set up an Azure AD application and get its client ID as well as the created secret value.

Either way (by using PresenceLight which in turn uses the same Microsoft Ggraph API) or the Microsotft Graph API directly yourselves, you can obtain the status/presence information to use with this app:

set Flask app environment variable:
export FLASK_APP=app.py

Then run with: 
flask run --host=0.0.0.0

If it's working on 127.0.0.0:5000, you can chnage your LCD display to  reflect your status info by this:

http://127.0.0.1:5000/status/available or 
http://127.0.0.1:5000/status/busy
http://127.0.0.1:5000/status/present

Other supported status messages to display are in the app.py.

I am running this app on a Raspbery Pi 2 which has an LCD display connected. Any problems just report / create an issues and/or a pull request.