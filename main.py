import requests
import twython
from datetime import datetime as dt

mona = requests.get('https://api.zaif.jp/api/1/last_price/mona_jpy')

crypts = mona.json()

with open("twi.api", "r")as ap:
    API_KEY = ap.readline().strip()
    API_SEC = ap.readline().strip()
    TOC = ap.readline().strip()
    TOC_KEY = ap.readline().strip()

api = twython.Twython(app_key=API_KEY,
                      app_secret=API_SEC,
                      oauth_token=TOC,
                      oauth_token_secret=TOC_KEY)
now = dt.now()
with open("yesterday.txt", "r")as yes:
    yesmona = float(yes.read())

nowmona = crypts["last_price"]

wari = nowmona / yesmona
if wari >= 1:
    prm = '+'
else:
    prm = '-'
    wari = 1 - wari
    
api.update_status(status="Monacoinの価格 : "
                  +str(nowmona)
                  +" 円\n"
                  +"昨日比 : "
                  +prm
                  +str(int(wari*100))
                  +"%"
                  +now.strftime('(%H:%M現在)'))

with open("kakaku.txt", "w")as file:
    file.write(str(nowmona)
               +"\n"
               +now.strftime('%H:%M'))

with open("updw.txt", "w")as pya:
    pya.write("1")

time = now.strtime('%H:%M')
if time == '00:00':
    with open("yesterday.txt", "w")as chan:
        chan.write(str(nowmona))
