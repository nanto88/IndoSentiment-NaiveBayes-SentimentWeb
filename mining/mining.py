import tweepy
from tweepy import OAuthHandler
import csv
from textblob import TextBlob

TWEEPY_CONSUMER_KEY = '...'
TWEEPY_CONSUMER_SECRET = '...'
TWEEPY_ACCESS_TOKEN_KEY = '...'
TWEEPY_ACCESS_TOKEN_SECRET = '...'

auth = OAuthHandler(TWEEPY_CONSUMER_KEY, TWEEPY_CONSUMER_SECRET)
auth.set_access_token(TWEEPY_ACCESS_TOKEN_KEY, TWEEPY_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

#def process_or_store(tweet):
 #   print(json.dumps(tweet))

query = 'Elon Musk'
max_tweets = 10

#with open('sentiment.csv', 'w', newline='', encoding='utf-8') as f:
        #thewriter = csv.writer(f)
for tweet in tweepy.Cursor(api.search, q=query, lang="eng", show_user="true").items(max_tweets):
#process single status
    #if not tweet.retweeted and 'RT @' not in tweet.text:
        print(tweet.text)
        print(TextBlob(tweet.text).sentiment)
        print(tweet.user.screen_name)
        print("============================")
            
            #for csv write
            #thewriter.writerow([tweet.text, 0])
