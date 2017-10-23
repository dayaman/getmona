import requests
import twython

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

def judge(num):
    if num >= 0.05:
        return True
    else:
        return False
    
def main():
    with open("kakaku.txt", "r")as old:
        kari = old.readline().strip()
        time = old.readline().strip()
    kakaku = float(kari)
    nowpr = crypts["last_price"]
    wari = nowpr / kakaku
    with open("updw.txt", "r")as jud:
        getju  = jud.read()
        han = float(getju)
        if wari >= 1:
            tast = wari - han
            getj = judge(tast)
            kouk = "高騰中"
            prm = "+"
        else:
            tast = han - wari
            getj = judge(tast)
            kouk = "下落中"
            prm = ""
    if getj == True:
        api.update_status(status="Monacoin"
                          +kouk
                          +"\n現在 "
                          +str(crypts["last_price"])
                          +" 円\n"
                          +time
                          +"比:"
                          +prm
                          +str(int((wari-1)*100))
                          +"%")
        with open("updw.txt", "w")as pya:
            
            pya.write("%.1f" % wari)

if __name__ == '__main__':
    main()
