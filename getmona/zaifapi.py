import threading
from time import sleep
from datetime import datetime
from getmona import db
from getmona.models import Price
import json
import websocket

price={}

def start_threading():
    thread_a=threading.Thread(target=getprice, args=('mona_jpy',))
    thread_a.start()
    getprice('mona_btc')
    
def getprice(pair):
    global price
    name=pair
    thread1=threading.Thread(target=connws, args=(name,))
    thread1.start()
    sleep(5)
    while True:
        rec_price(price[name])
        sleep(1)

def rec_price(rc):
    money=rc['last_price']['price']
    pair_name=rc['currency_pair']
    kakaku=Price.query.get(pair_name)
    kakaku.latest_price=money
    db.session.add(kakaku)
    db.session.commit()
    
def connws(pair):
    global price
    ws=websocket.create_connection('wss://ws.zaif.jp:8888/stream?currency_pair='+pair)
    while True:
        try:
            ws.send('payload')
            price[pair]=json.loads(ws.recv())
        except:
            is_connect = False
            while is_connect == False:
                try:
                    sleep(10)
                    ws=websocket.create_connection('wss://ws.zaif.jp:8888/stream?currency_pair='+pair)
                    is_connect = True
                except Exception as err2:
                    write_log(err2)
            
        sleep(1)
        
def write_log(errob):
        logf = open('log/zaifapi.log', 'a')
        dt_now = datetime.now()
        str_dt = dt_now.strftime('%Y-%m-%d %H:%M:%S')
        logf.write(str_dt+' '+str(errob)+'\n')
        logf.close()
