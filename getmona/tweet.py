import twython

with open("getmona/twi.api", "r")as ap:
        API_KEY = ap.readline().strip()
        API_SEC = ap.readline().strip()
        TOC = ap.readline().strip()
        TOC_KEY = ap.readline().strip()

api = twython.Twython(app_key=API_KEY,
                      app_secret=API_SEC,
                      oauth_token=TOC,
                      oauth_token_secret=TOC_KEY)
    
def tweet(saytw):
    api.update_status(status=saytw)

def follow():
        search_results = api.search(q='モナコイン -RT', count=8)
        results = search_results['statuses']
        for result in results:
                user_id = result['user']['screen_name']
                api.create_friendship(screen_name=user_id)
