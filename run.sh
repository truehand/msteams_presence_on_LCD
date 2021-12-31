ps -ef|grep "flask run"|tr -s " "|cut -d " " -f 2| head -1| xargs kill
git pull
sleep 3
export FLASK_ENV=development
export FLASK_APP=presence_server.py
mkdir -p logs
nohup flask run -h 0.0.0.0 -p 5000 2>logs/err.txt 1>logs/log.txt&