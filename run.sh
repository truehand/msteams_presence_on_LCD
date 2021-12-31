echo killing a previous potential Flask session...
ps -ef|grep "flask run"|tr -s " "|cut -d " " -f 2| head -1| xargs kill
sleep 1
acho pulling the latest code...
git pull
sleep 2
echo running the Flask application on port 5000...
export FLASK_ENV=development
export FLASK_APP=presence_server.py
mkdir -p logs
nohup flask run -h 0.0.0.0 -p 5000 2>logs/err.txt 1>logs/log.txt&
echo logs are in logs/log.txt and logs/err.txt
echo done.