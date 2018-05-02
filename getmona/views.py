import flask
from getmona import app, db
from getmona.models import Price
import threading
from zaifapi import start_threading

thread_a = threading.Thread(target=start_threading)
thread_a.start()

@app.route('/regularly')

@app.route('/follow')
