import json
#import websocket as web
import requests
from datetime import datetime as dt
import tweepy

with open("twi.api", "r")as ap:
    API_KEY = ap.readline().strip()
    API_SEC = ap.readline().strip()
    TOC = ap.readline().strip()
    TOC_KEY = ap.readline().strip()

consumer_key=API_KEY
consumer_secret=API_SEC
key=TOC
secret=TOC_KEY

auth = tweepy.OAuthHandler(API_KEY, API_SEC)
auth.set_access_token(TOC, TOC_KEY)

api = tweepy.API(auth)

mona_jpy = 0
mona_btc = 0

def get(money): #wssが不調なので、暫定処置
    if money == "jpy":
        #ws_jpy = web.create_connection("wss://ws.zaif.jp:8888/stream?currency_pair=mona_jpy")
        #ws = ws_jpy
        mona = requests.get('https://api.zaif.jp/api/1/last_price/mona_jpy')

    else:
        #ws_btc = web.create_connection("wss://ws.zaif.jp:8888/stream?currency_pair=mona_btc")
        #ws = ws_btc
        mona = requests.get('https://api.zaif.jp/api/1/last_price/mona_btc')

    crypts = mona.json()
    price = crypts["last_price"]
    """
    result = ws.recv()
    status = json.loads(result)
    price_status = status["last_price"]
    price = price_status["price"]
    ws.close()"""
    return price

class Listener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
        status_id = status.id
        now = dt.now()
        #print(now)
        time = now.strftime('%H:%M:%S')
        #print(time)
        user_id = str(status.user.screen_name)
        #print(user_id)
        if user_id != "kakaku_mona":
            twein = ("""@%s モナコインの価格は\n%.1f円\n%fBTC\nです。(%s現在)"""
                     % ( user_id, get("jpy"), get("btc"), time))
        #print(twein)
        api.update_status(status=twein, in_reply_to_status_id=status_id)
    
def main():
    myStreamListener = Listener()
    myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
    #myStream.filter(track=['@kakaku_mona'])

    #"""
    while True:
        try:
            myStream.filter(track=['@kakaku_mona'])
        except:
            pass
    #""""
        
if __name__=='__main__':
    main()
