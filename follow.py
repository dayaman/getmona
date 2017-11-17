import tweepy

with open("twi.api", "r")as ap:
    API_KEY = ap.readline().strip()
    API_SEC = ap.readline().strip()
    TOC = ap.readline().strip()
    TOC_KEY = ap.readline().strip()

auth = tweepy.OAuthHandler(API_KEY, API_SEC)
auth.set_access_token(TOC, TOC_KEY)

api = tweepy.API(auth)

def main():
    for status in api.search(q="モナコイン -RT",count=8):
        user_id = str(status.user.screen_name)
        try:
            api.create_friendship(user_id)
        except:


if __name__=='__main__':
    main()
