import tweepy
from os import environ

CONSUMER_SECRET = environ("CONSUMER_SECRET")
CONSUMER_KEY = environ("CONSUMER_KEY")
ACCESS_TOKEN = environ("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = environ("ACCESS_TOKEN_SECRET")

apikeys = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
apikeys.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(apikeys, wait_on_rate_limit_notify=True)




