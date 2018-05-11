import flask
from getmona import app
from getmona.regularly import tweet_regularly
from getmona.tweet import follow

@app.route('/regularly')
def regularly():
    tweet_regularly()
    return '200'
        
@app.route('/follow')
def following():
    follow()
    return '200'
