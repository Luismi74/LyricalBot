import tweepy
import os

CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

apikeys = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
apikeys.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(apikeys, wait_on_rate_limit_notify=True)




