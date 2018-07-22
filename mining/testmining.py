import tweepy
from tweepy import OAuthHandler
import csv
#from textblob import TextBlob
#from textblob.sentiments import NaiveBayesAnalyzer
from stopwords import preprocess_tweet
from ftfy import fix_text


TWEEPY_CONSUMER_KEY = '...'
TWEEPY_CONSUMER_SECRET = '...'
TWEEPY_ACCESS_TOKEN_KEY = '...'
TWEEPY_ACCESS_TOKEN_SECRET = '...'

auth = OAuthHandler(TWEEPY_CONSUMER_KEY, TWEEPY_CONSUMER_SECRET)
auth.set_access_token(TWEEPY_ACCESS_TOKEN_KEY, TWEEPY_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

query = "piala dunia"
max_tweets = 100

"""
for tweet in tweepy.Cursor(api.search, q=query, lang="id", show_user="true").items(max_tweets):
   # if not tweet.retweeted and 'RT @' not in tweet.text:
        print("============================")
        print("Ver: Ori")
        texts = fix_text(tweet.text)
        print(texts)
        print("============================")
        print("Ver: Clean")
        print(preprocess_tweet(texts))
        #print(TextBlob(tweet.text, analyzer=NaiveBayesAnalyzer()).sentiment)
        print("============================")
        print(tweet.user.screen_name)
        print("============================")
        #"""
rt = 0
with open('pilgub.csv', 'a', newline='', encoding='UTF-8') as f:
    thewriter = csv.writer(f)
#    first write csv
    thewriter.writerow(["tweet","clean_tweet","sentiment"])
    for tweet in tweepy.Cursor(api.search, q=query+"-filter:retweets", lang="id", show_user="true", since='2018-06-04', until='2018-07-09').items(max_tweets):
#process single status
        if 'RT ' not in tweet.text:
            rt = rt + 1
            
        texts = fix_text(tweet.text, remove_terminal_escapes=True, remove_bom=True, remove_control_chars=True)
        if '…' in texts:
            texts = texts.rsplit(' ', 1)[0]
        #remove symbol unicode
        texts = texts.encode('ascii', 'ignore').decode('utf-8')
        """
        if preprocess_tweet(texts) == ' ':
            continue
        if preprocess_tweet(texts) == '':
            continue      
        """
        print("============================")
        print(tweet.retweeted)
        print("============================")
        print("Ver: Ori")
        print(texts)
        print("============================")
        print("Ver: Clean")
        print(preprocess_tweet(texts))
        print("============================")
        print(tweet.user.screen_name)
        print("============================")
        clean_tweet = preprocess_tweet(texts)
            #for csv write
        thewriter.writerow([tweet.text,clean_tweet, 0])