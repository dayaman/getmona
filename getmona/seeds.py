import requests
from getmona import db
from getmona.models import Price

def addpair():
    add_to_db("mona_jpy")
    add_to_db("mona_btc")

def add_to_db(nmoney):
    jmona = requests.get('https://api.zaif.jp/api/1/last_price/' + nmoney)
    mona = jmona.json()
    lastmona = mona['last_price']
    price = Price(pair=nmoney, yesterday_price=lastmona)
    db.session.add(price)
    db.session.commit()











