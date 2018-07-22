#Config
import tweepy
from tweepy import OAuthHandler

TWEEPY_CONSUMER_KEY = '...'
TWEEPY_CONSUMER_SECRET = '...'
TWEEPY_ACCESS_TOKEN_KEY = '...'
TWEEPY_ACCESS_TOKEN_SECRET = '...'

def twitterApi():
    auth = OAuthHandler(TWEEPY_CONSUMER_KEY, TWEEPY_CONSUMER_SECRET)
    auth.set_access_token(TWEEPY_ACCESS_TOKEN_KEY, TWEEPY_ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    return api