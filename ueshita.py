import json
import requests
import twython
from websocket import *
import time
from datetime import datetime as dt

with open("twi.api", "r")as ap:
    API_KEY = ap.readline().strip()
    API_SEC = ap.readline().strip()
    TOC = ap.readline().strip()
    TOC_KEY = ap.readline().strip()

api = twython.Twython(app_key=API_KEY,
                      app_secret=API_SEC,
                      oauth_token=TOC,
                      oauth_token_secret=TOC_KEY)

lastwari_jpy = 0
lastwari_btc = 0

nowtime = ""

def judge(money,num):
    if money == "jpy":
        if lastwari_jpy >= 0 and num < 0:
            return True
        elif lastwari_jpy < 0 and num > 0:
            return True
        
        if lastwari_jpy >= 0 and num >= 0:
            if num - lastwari_jpy >= 1:
                return True
            else:
                return False
        else:
            if num - lastwari_jpy <= -1:
                return True
            else:
                return False
    else:
        if lastwari_btc >= 0 and num < 0:
            return True
        elif lastwari_btc < 0 and num > 0:
            return True

        if lastwari_btc >= 0 and num >= 0:
            if num - lastwari_btc >= 1:
                return True
            else:
                return False
        else:
            if num - lastwari_btc <= -1:
                return True
            else:
                return False
        

def get_price(money):
    if money == "jpy":
        ws = ws_jpy
        ws_jpy = create_connection("wss://ws.zaif.jp:8888/stream?currency_pair=mona_jpy")
    else:
        ws = ws_btc
        ws_btc = create_connection("wss://ws.zaif.jp:8888/stream?currency_pair=mona_btc")
    
    result = ws.recv()
    status = json.loads(result)
    price_status = status["last_price"]
    price = price_status["price"]
    ws.close()
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
    try:
        api.update_status(status="mona_"
                              +money
                              +kouk
                              +"\n現在 "
                              +str(price)
                              +tani
                              +"\n"
                              +"昨日比:"
                              +"%+d%%" % per
                              +"("+nowtime+"現在)"
                              )
    
    except:
        pass

def main():
    while True:

        global lastwari_jpy
        global lastwari_btc
        global nowtime
        
        now = dt.now()
        nowtime = now.strftime('%H:%M')
        
        
        with open("yesterday.txt", "r")as yes:
            yesmona_jpy = float(yes.readline().strip())
            yesmona_btc = float(yes.readline().strip())
        
        if nowtime == "00:00":
            lastwari_jpy = 0
            lastwari_btc = 0
        
        mona_jpy = float(get_price("jpy"))
        mona_btc = float(get_price("btc"))
        wari_jpy = mona_jpy / yesmona_jpy
        wari_btc = mona_btc / yesmona_btc
        per_jpy = int((wari_jpy - 1) * 100) // 5
        per_btc = int((wari_btc - 1) * 100) // 5
                    
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
