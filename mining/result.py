import csv
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from stopwords import preprocess_tweet

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()
stemmer.stem("teristimewa")

def clean(tweet):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    clean = stemmer.stem(preprocess_tweet(tweet))
    return clean
from stopwords import preprocess_tweet

tweet = "PILGUB JABAR 2018: Ridwan Kamil-Uu Belum Bisa Ditetapkan Sebagai Pemenang. Ini Sebabnya #ridwankamil #rindujabar"
clean(tweet)
stemmer.stem().stem(preprocess_tweet(tweet))

textblob = []
pos = 0
neg = 0
net = 0
with open('pilgub_stem2.csv','r', encoding='utf8') as f:
    thereader = csv.reader(f)
    for row in thereader:
        if row[2] == "clean_tweet":
            continue
        if row[3] == '0':
            neg += 1
        if row[3] == '1':
            pos += 1
        if row[3] == '2':
            net += 1
        tblob = row[2],row[3]
        textblob.append(tblob)


#save csv
with open('pilgub.csv','r', encoding='utf8') as f:
    thereader = csv.reader(f)
    with open('pilgub_stem2.csv','w', newline='', encoding='utf8') as w:
        thewriter = csv.writer(w)
        for row in thereader:
            thewriter.writerow([row[0],row[1],stemmer.stem(row[1]),row[2]])


"""
# stemming process
sentence = 'Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan'
output   = stemmer.stem(sentence)

print(output)
# ekonomi indonesia sedang dalam tumbuh yang bangga
"""

        
from sklearn.cross_validation import train_test_split
X_train, X_test = train_test_split(textblob, test_size = 0.2, random_state = 80)

from textblob.classifiers import NaiveBayesClassifier
clf = NaiveBayesClassifier(textblob)
clf.accuracy(X_test)


testing = 'Presiden rindujabarjuara etis rusuh'
clean_test = preprocess_tweet(testing)
prob_dist = clf.prob_classify(blob)

pos_prob = round(prob_dist.prob("1"), 2)
neg_prob = round(prob_dist.prob("0"), 2)

print(float(round(prob_dist.prob("0"), 2)))

round(prob_dist.prob("1"), 2)
round(prob_dist.prob("2"), 2)

clf.show_informative_features(15)

#testing
from textblob import TextBlob
asd = TextBlob("garut kunjungannya kali kang emil team berkeliling banyuresmi rindujabarjuara", classifier=clf)
#blob.classify()
text_test = 'garut kunjungannya kali kang emil team berkeliling banyuresmi rindujabarjuara'
prob_dist = clf.prob_classify(text_test)

import pickle
from sklearn.externals import joblib   
file = open('pilgubstem.obj', 'wb')
joblib.dump(clf, file)
file.close()

with open('pilgubstem.obj', 'rb') as p:
    model3 = joblib.load(p)
model2 = pickle.load('pilgubstem.obj', 'rb')
model2.classify("ini kalo menang bagus sih ya ga haha")