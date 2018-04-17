import time
import json
import websocket

def getjpy():
    ws_jpy=websocket.create_connection('wss://ws.zaif.jp:8888/stream?currency_pair=mona_jpy')
    ws_jpy.send('payload')
    result=json.loads(ws_jpy.recv())
    price_jpy=result['last_price']['price']
    ws_jpy.close()
    return price_jpy

def getbtc():
    ws_btc=websocket.create_connection('wss://ws.zaif.jp:8888/stream?currency_pair=mona_btc')
    ws_btc.send('payload')
    result=json.loads(ws_btc.recv())
    price_btc=result['last_price']['price']
    ws_jpy.close()
    return price_btc
