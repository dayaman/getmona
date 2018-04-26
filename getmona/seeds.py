from getmona import db
from getmona.models import Price

def addpair():
    add_to_db("mona_jpy")
    add_to_db("mona_btc")

def add_to_db(nmoney):
    price = Price(pair=nmoney)
    db.session.add(price)
    db.session.commit()

