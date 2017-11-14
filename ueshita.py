import json
import requests
import twython
from websocket import *
import time
from datetime import datetime as dt

ws_jpy = create_connection("wss://ws.zaif.jp:8888/stream?currency_pair=mona_jpy")
ws_btc = create_connection("wss://ws.zaif.jp:8888/stream?currency_pair=mona_btc")


with open("twi.api", "r")as ap:
    API_KEY = ap.readline().strip()
    API_SEC = ap.readline().strip()
    TOC = ap.readline().strip()
    TOC_KEY = ap.readline().strip()

api = twython.Twython(app_key=API_KEY,
                      app_secret=API_SEC,
                      oauth_token=TOC,
                      oauth_token_secret=TOC_KEY)

with open("yesterday.txt", "r")as yes:
    yesmona_jpy = float(yes.readline().strip())
    yesmona_btc = float(yes.readline().strip())

now = dt.now()
nowtime = now.strftime('%H:%M')

lastwari_jpy = 0
lastwari_btc = 0

def judge(money,num):
    if money == "jpy":
        if lastwari_jpy >= 0 and num < 0:
            return True
        elif lastwari_jpy < 0 and num >= 0:
            return True
        
        if abs(num - lastwari_jpy) > 1:
            return True
        else:
            return False
    else:
        if lastwari_btc >= 0 and num < 0:
            return True
        elif lastwari_btc < 0 and num >= 0:
            return True
        
        if abs(num - lastwari_btc) >= 1:
            return True
        else:
            return False

def get_price(money):
    if money == "jpy":
        ws = ws_jpy
    else:
        ws = ws_btc

    result = ws.recv()
    status = json.loads(result)
    price_status = status["last_price"]
    price = price_status["price"]
    return price

def tweet(money,price,per):
    if money == "jpy":
        tani = "円"
    else:
        tani = "BTC"

    if per >= 0:
        kouk = "上昇中"
    else:
        kouk = "下降中"

    per *= 5
    api.update_status(status="mona_"
                              +money
                              +kouk
                              +"\n現在 "
                              +str(price)
                              +tani
                              +"\n"
                              +"昨日比:"
                              +"%+d%%" % per
                              )

def main():
    while nowtime != '00:00':

        global lastwari_jpy
        global lastwari_btc
        
        mona_jpy = float(get_price("jpy"))
        mona_btc = float(get_price("btc"))
        wari_jpy = mona_jpy / yesmona_jpy
        wari_btc = mona_btc / yesmona_btc
        per_jpy = (wari_jpy - 1) * 100 // 5
        per_btc = (wari_btc - 1) * 100 // 5
                    
        jd_jpy = judge("jpy", per_jpy)
        jd_btc = judge("btc", per_btc)

        
        if jd_jpy == True:
            tweet("jpy", mona_jpy, per_jpy)
            lastwari_jpy = per_jpy
                
        if jd_btc == True:
            tweet("btc", mona_btc, per_btc)
            lastwari_btc = per_btc
            
        time.sleep(5)
    ws_jpy.close()
    ws_btc.close()
if __name__ == '__main__':
    main()
