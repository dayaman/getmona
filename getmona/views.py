import flask
from getmona import app, db
from getmona.models import Price
import threading
from getmona.zaifapi import start_threading
from getmona.regularly import tweet_regularly
from getmona.tweet import follow

@app.route('/regularly')
def regularly():
    tweet_regularly()
    
@app.route('/follow')
def following():
    follow()
