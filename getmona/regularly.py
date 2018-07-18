from getmona.tweet import tweet
from datetime import datetime as dt
from getmona import db
from getmona.models import Price

def tweet_regularly():
    jpy = Price.query.get('mona_jpy')
    btc = Price.query.get('mona_btc')
    nmona_jpy = jpy.latest_price
    nmona_btc = btc.latest_price

    now = dt.now()

    time = now.strftime('%H:%M')
    if time == '00:00':
        rec_yes(jpy)
        rec_yes(btc)
    
    ymona_jpy = jpy.yesterday_price
    ymona_btc = btc.yesterday_price

    per_jpy = wariai(nmona_jpy, ymona_jpy)
    per_btc = wariai(nmona_btc, ymona_btc)
    
    tweet("Monacoinの価格\n"
          +str(nmona_jpy)
          +"円(昨日比:"
          +'%+d' % per_jpy
          +"%)\n"
          +str(nmona_btc)
          +"BTC(昨日比:"
          +'%+d' % per_btc
          +"%)\n"
          +now.strftime('(%H:%M現在)'))

def rec_yes(nmoney):
    nmoney.yesterday_price = nmoney.latest_price
    db.session.add(nmoney)
    db.session.commit()

def wariai(now, yes):
    wari = now / yes
    per = int((wari - 1) * 100)
    return per























