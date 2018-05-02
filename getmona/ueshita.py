import time
from datetime import datetime
from getmona import db
from getmona.models import Price
from getmona.tweet import tweet

def loop_get():
    mae_jpy = 0
    mae_btc = 0
    while True:
        mae_jpy = get_ratio('mona_jpy', mae_jpy)
        mae_btc = get_ratio('mona_btc', mae_btc)
        sleep(1)
        
def get_ratio(nmoney, mae):
    mona = Price.query.get(nmoney)
    per = ((mona.latest_price / mona.yesterday_price) * 100 - 100) // 5
    judge = is_Tweet(per, mae)

def is_Tweet(per, mae):
    if per > 0:
        if mae < 0:
            return True
        if per - mae >= 1:
            return True
    elif per < 0:
        pass
