echo killing previous potential Flask sessions...
pkill -9 -f "flask run"
echo pulling the latest code...
git pull
sleep 2
echo running the Flask application on port 5000...
export FLASK_ENV=development
export FLASK_APP=presence_server.py
mkdir -p logs
nohup flask run -h 0.0.0.0 -p 5000 2>>logs/err.txt 1>>logs/log.txt&
echo watch logs with:
echo tail -f logs/log.txt logs/err.txt
echo done.