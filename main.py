import requests
#import twython
import tweet
from datetime import datetime as dt

mona = requests.get('https://api.zaif.jp/api/1/last_price/mona_jpy')
monabtc = requests.get('https://api.zaif.jp/api/1/last_price/mona_btc')

crypts = mona.json()
crypts_btc = monabtc.json()

# with open("twi.api", "r")as ap:
#     API_KEY = ap.readline().strip()
#     API_SEC = ap.readline().strip()
#     TOC = ap.readline().strip()
#     TOC_KEY = ap.readline().strip()

# api = twython.Twython(app_key=API_KEY,
#                       app_secret=API_SEC,
#                       oauth_token=TOC,
#                       oauth_token_secret=TOC_KEY)

nowmona = crypts["last_price"]
nowmona_btc = crypts_btc["last_price"]

now = dt.now()

time = now.strftime('%H:%M')
if time == '00:00':
    with open("yesterday.txt", "w")as chan:
        chan.write(str(nowmona)+
                   '\n'+
                   str(nowmona_btc))

with open("yesterday.txt", "r")as yes:
    yesmona = float(yes.readline().strip())
    yesmona_btc = float(yes.readline().strip())

wari = nowmona / yesmona
if wari >= 1:
    prm = '+'
    wari = int((wari - 1) * 100)
else:
    prm = '-'
    wari = int((1 - wari) * 100)

wari_btc = nowmona_btc / yesmona_btc
if wari_btc >= 1:
    prm_btc = '+'
    wari_btc = int((wari_btc - 1) * 100)
else:
    prm_btc = '-'
    wari_btc = int((1 - wari_btc) * 100)


#api.update_status(status="Monacoinの価格\n"
tweet.tweet("Monacoinの価格\n"
            +str(nowmona)
            +"円(昨日比:"
            +prm
            +str(wari)
            +"%)\n"
            +str(nowmona_btc)
            +"BTC(昨日比:"
            +prm_btc
            +str(wari_btc)
            +"%)\n"
            +now.strftime('(%H:%M現在)'))
