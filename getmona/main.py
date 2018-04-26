import tweet
from datetime import datetime as dt

nowmona = crypts["last_price"]
nowmona_btc = crypts_btc["last_price"]

now = dt.now()

time = now.strftime('%H:%M')
if time == '00:00':
    with open("yesterday.txt", "w")as chan:
        chan.write(str(nowmona)+
                   '\n'+
                   str(nowmona_btc))

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
