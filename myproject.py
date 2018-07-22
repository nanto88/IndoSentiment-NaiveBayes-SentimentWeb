from flask import Flask, render_template, request
from tweet.config import twitterApi
from mining.stopwords import preprocess_tweet
from mining.dateformat import sinceDate, untilDate
from sklearn.externals import joblib
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import pickle
import tweepy
import time

app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)


api = twitterApi()




def t():
    return round(time.clock(), 2)
def cleanquery(query):    
    if "-filter:retweets" in query:
        return query[:-16]
    else:
        return query
app.jinja_env.globals.update(t=t, cleanquery=cleanquery)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sentiment', methods=['GET', 'POST'])
def sentiment():
    
    
    if request.method=='POST':
        query = request.form['query']
        daterange = request.form['daterange']
        nort = request.form.get('nort')
        stem = request.form.get('stem')
        
        t0 = time.clock()
        
        if stem:
            with open('static/pilgubstem2.pkl', 'rb') as f:
                model = pickle.load(f)
            def clean(tweet):
                factory = StemmerFactory()
                stemmer = factory.create_stemmer()
                clean = stemmer.stem(preprocess_tweet(tweet))
                return clean
            app.jinja_env.globals.update(clean=clean)
            t1 = time.clock()
        else:
            with open('static/pilgub.pkl', 'rb') as f:
                model = pickle.load(f)
            def clean(tweet):
                return preprocess_tweet(tweet)
            app.jinja_env.globals.update(clean=clean)
            t1 = time.clock()
        
        est = round(t1, 2)-round(t0, 2)
        
        if nort:
            query=query+"-filter:retweets"
        
        if daterange=="":
            tweets = tweepy.Cursor(api.search, q=query, lang="id", show_user="true").items(100)
        else:
            tweets = tweepy.Cursor(api.search, q=query, lang="id", show_user="true", since=sinceDate(daterange), until=untilDate(daterange)).items(100)
      
    return render_template('sentiment.html', tweets=tweets, model=model, est=est, query=query)




if __name__ == '__main__':
    app.run(host='0.0.0.0')
