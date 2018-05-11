import twython
from getmona.make_reply import make_text
from datetime import datetime

with open("getmona/twi.api", "r")as ap:
        API_KEY = ap.readline().strip()
        API_SEC = ap.readline().strip()
        TOC = ap.readline().strip()
        TOC_KEY = ap.readline().strip()

api = twython.Twython(app_key=API_KEY,
                      app_secret=API_SEC,
                      oauth_token=TOC,
                      oauth_token_secret=TOC_KEY)

class Listener(twython.TwythonStreamer):
        def on_success(self, status):
                status_id = status['id']
                user_screen_name = status['user']['screen_name']
                if user_screen_name != "kakaku_mona":
                        text_rep  = make_text(status)
                        tweet(text_rep, status_id)

def get_reply():
        while True:
                try:
                        stream = Listener(API_KEY, API_SEC, TOC, TOC_KEY)
                        stream.statuses.filter(track='@kakaku_mona')
                except KeyboardInterrupt:
                        exit(-1)
        
def tweet(saytw, id=-1):
        try:
                if id == -1:
                        api.update_status(status=saytw)
                else:
                        api.update_status(status=saytw, in_reply_to_status_id=id)   
        except Exception as e:
                write_log(e)

def follow():
        search_results = api.search(q='モナコイン -RT', count=8)
        results = search_results['statuses']
        for result in results:
                user_id = result['user']['screen_name']
                if user_id != 'kakaku_mona':
                        try:
                                api.create_friendship(screen_name=user_id)
                        except Exception as e:
                                write_log(e)

def write_log(errob):
        logf = open('log/tweet.log', 'a')
        dt_now = datetime.now()
        str_dt = dt_now.strftime('%Y-%m-%d %H:%M:%S')
        logf.write(str_dt+' '+str(errob)+'\n')
        logf.close()
