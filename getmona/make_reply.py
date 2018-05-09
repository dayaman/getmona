from datetime import datetime
from getmona import db
from getmona.models import Price

def make_text(status):
    jpy = Price.query.get('mona_jpy')
    btc = Price.query.get('mona_btc')
    db.session.refresh(jpy)
    db.session.refresh(btc)

    now = datetime.now()
    time = now.strftime('%H:%M:%S')

    user_id = status['user']['screen_name']
    reply = ("""@%s モナコインの価格は\n%.1f円\n%fBTC\nです。(%s現在)"""
             % (user_id, jpy.latest_price, btc.latest_price, time))
    return reply
