import json
import websocket as web
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

def get(money):
    if money == "jpy":
        ws = ws_jpy
        ws_jpy = web.create_connection("wss://ws.zaif.jp:8888/stream?currency_pair=mona_jpy")
    else:
        ws = ws_btc
        ws_btc = web.create_connection("wss://ws.zaif.jp:8888/stream?currency_pair=mona_btc")

    result = ws.recv()
    status = json.loads(result)
    price_status = status["last_price"]
    price = price_status["price"]
    ws.close()
    return price

class Listener(tweepy.StreamListener):
    def on_status(self, status):
        #print(status.text)
        status_id = status.id
        now = dt.now()
        #print(now)
        time = now.strftime('%H:%M:%S')
        #print(time)
        user_id = str(status.user.screen_name)
        #print(user_id)
        twein = ("""@%s モナコインの価格は\n%.1f円\n%fBTC\nです。(%s現在)"""
                 % ( user_id, get("jpy"), get("btc"), time))
        #print(twein)
        api.update_status(status=twein, in_reply_to_status_id=status_id)
    
def main():
    myStreamListener = Listener()
    myStream = tweepy.Stream(auth = api.auth, listener =Listener())
    #myStream.filter(track=['@kakaku_monatest'])
    while True:
        try:
            myStream.filter(track=['@kakaku_mona'])
        except:
            pass
        
if __name__=='__main__':
    main()
