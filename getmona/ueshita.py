from time import sleep
from datetime import datetime
from getmona import db
from getmona.models import Price
from getmona.tweet import tweet

class Updw():
    def __init__(self, nmoney, mae):
        self.nmoney = nmoney
        self.mae = mae

    def get_raito(self):
        mona = Price.query.get(self.nmoney)
        db.session.refresh(mona)
        self.per = ((mona.latest_price / mona.yesterday_price) * 100 - 100) // 5
        judge = self.is_Tweet()
        if judge == True:
            do_tweet(self)

    def is_Tweet(self):
        mae = self.mae
        per = self.per
    
        if per > 0:
            if mae < 0:
                self.mae = per
                return True
            if per - mae >= 1:
                self.mae = per
                return True
        elif per < 0:
            if mae > 0:
                self.mae = per
                return True
            if per - mae <= -1:
                self.mae = per
                return True
        return False
    
def loop_get():
    jpy = Updw('mona_jpy', 0)
    btc = Updw('mona_btc', 0)
    while True:
        jpy.get_raito()
        btc.get_raito()
        sleep(1)    

def do_tweet(currency):
    if currency.per > 0:
        up_or_dw = '上昇中'
    else:
        up_or_dw = '下降中'

    tani = {
        'mona_jpy': '円',
        'mona_btc': 'BTC'
    }
    mona = Price.query.get(currency.nmoney)
    now = datetime.now()
    nowtime = now.strftime('%H:%M')
    
    tw_str = currency.nmoney \
             + up_or_dw \
             + '\n現在' \
             + str(mona.latest_price) \
             + tani[currency.nmoney] \
             + '\n昨日比' \
             + '%+d%%' % (currency.per * 5) \
             + '(' \
             + nowtime \
             +'現在)'
             
    tweet(tw_str)
