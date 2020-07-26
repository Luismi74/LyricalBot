import tweepy
from os import environ

CONSUMER_SECRET = os.environ("CONSUMER_SECRET")
CONSUMER_KEY = os.environ("CONSUMER_KEY")
ACCESS_TOKEN = os.environ("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ("ACCESS_TOKEN_SECRET")

apikeys = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
apikeys.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(apikeys, wait_on_rate_limit_notify=True)




