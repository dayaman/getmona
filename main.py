import requests
import twython
from datetime import datetime as dt

mona = requests.get('https://api.zaif.jp/api/1/last_price/mona_jpy')

crypts = mona.json()

with open("kakaku.txt", "w")as file:
    file.write(str(crypts["last_price"]))

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
api.update_status(status="現在のMonacoinの価格 : "
                  +str(crypts["last_price"])
                  +" 円\n"
                  +now.strftime('(%H:%M現在)'))
