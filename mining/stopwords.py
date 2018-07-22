import re
from ftfy import fix_text
"""
stop_words2 = []
infile = open('stopword_list_tala_v2.txt', 'r')
for word in infile:
    stop_words2.append(word.strip('\n'))
infile.close()
print(stop_words2)


def reduce_lengthening(text):
    pattern = re.compile(r"(.)\1{1,}")
    return pattern.sub(r"\1\1", text)

lower_words = " @nanto88 ! , . &^% kayanya ada yang lagi senang ini. ini sepertinya"
#stop_words = ["the", "of", "a", "to", "be", "from", "or"]
last = lower_words.split()

print(reduce_lengthening(lower_words))


final = [word for word in last if word not in stop_words2]
final2 = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", lower_words).split())
final_join = " ".join(final)

"""
def stop_word():
    stop_words = []
    infile = open('mining/stopword_list_tala_v2.txt', 'r')
    for word in infile:
        stop_words.append(word.strip('\n'))
    infile.close()
    return stop_words

stop_words = stop_word()
  
def handle_emojis(tweet):
    # Smile -- :), : ), :-), (:, ( :, (-:, :')
    tweet = re.sub(r'(:\s?\)|:-\)|\(\s?:|\(-:|:\'\))', ' EMOPOS ', tweet)
    # Laugh -- :D, : D, :-D, xD, x-D, XD, X-D
    tweet = re.sub(r'(:\s?D|:-D|x-?D|X-?D)', ' EMOPOS ', tweet)
    # Love -- <3, :*
    tweet = re.sub(r'(<3|:\*)', ' EMOPOS ', tweet)
    # Wink -- ;-), ;), ;-D, ;D, (;,  (-;
    tweet = re.sub(r'(;-?\)|;-?D|\(-?;)', ' EMOPOS ', tweet)
    # Sad -- :-(, : (, :(, ):, )-:
    tweet = re.sub(r'(:\s?\(|:-\(|\)\s?:|\)-:)', ' EMONEG ', tweet)
    # Cry -- :,(, :'(, :"(
    tweet = re.sub(r'(:,\(|:\'\(|:"\()', ' EMONEG ', tweet)
    #haha
    tweet = re.sub(r'(ha){2,10}', ' EMOPOS ', tweet)
    #wkwk
    tweet = re.sub(r'(wk){2,10}', ' EMOPOS ', tweet)
    return tweet

def punctuations(tweet):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~0123456789=|'''
    no_punct = ""
    for char in tweet:
        if char not in punctuations:
            no_punct = no_punct + char
    return(no_punct)

def remove_sw(text):
    text_split = text.split()
    text_filter = [word for word in text_split if word not in stop_word()]
    text_join = " ".join(text_filter)    
    return text_join

def preprocess_tweet(tweet):
    # Convert to lower case
    tweet = tweet.lower()
    # Replaces URLs with the word URL
    tweet = re.sub('(www\.[^\s]+)|(\w+:\/\/\S+)', ' URL ', tweet)
    # Replace @handle with the word USER_MENTION
    tweet = re.sub(r'@[\S]+', 'USERMENTION', tweet)
    # Replaces #hashtag with hashtag
    tweet = re.sub(r'#(\S+)', r' \1 ', tweet)
    # Remove RT (retweet)
    tweet = re.sub(r'\brt\b', '', tweet)
    # Replace 2+ dots with space
    tweet = re.sub(r'\.{2,}', ' ', tweet)
    # Replace 2+ , with space
    tweet = re.sub(r'\,{2,}', ' ', tweet)
    # Strip space, " and ' from tweet
    tweet = tweet.strip(' "\'')
    # Replace multiple spaces with a single space
    tweet = re.sub(r'\s+', ' ', tweet)
    # funnnnny --> funny lengthening words
    tweet = re.sub(r'(.)\1+', r'\1\1', tweet)
    # Remove - & '
    tweet = re.sub(r'(-|\')', '', tweet)
    # Replace emojis with either EMO_POS or EMO_NEG
    tweet = handle_emojis(tweet)
    # Remove punctuations
    tweet = punctuations(tweet)
    # Remove Stopwords
    tweet = remove_sw(tweet)
    # Remove bug unicode
    tweet = tweet.replace('…', '')
    tweet = fix_text(tweet, remove_terminal_escapes=True, remove_bom=True, remove_control_chars=True)
    #remove symbol unicode
    tweet = tweet.encode('ascii', 'ignore').decode('utf-8')
    #tweet = tweet.replace('😂', '')
    #tweet = tweet.replace('❓', '')
    #tweet = tweet.replace('😛', '')
    #tweet = tweet.replace('•', '')
    #tweet = tweet.encode('ascii', 'ignore').decode('utf-8')
    return tweet

#tes = "funnny,, yeah!. @nanto ini cuma tes hahahahahahaha wkwk :) :( <3 http://asd.com www.asd.com https://www.asd.com"
#print(preprocess_tweet(tes))
"""
print(reduce_lengthening(lower_words))

tes = "funnny,, yeah!. @nanto ini cuma tes hahahahahahaha wkwk :) :( <3 http://asd.com www.asd.com https://www.asd.com"

print(preprocess_tweet(str))
print(preprocess_tweet(tes))
print(tes.strip( '!' ))

str = "!!!this is string example....wow!"
print (tes.strip( '''!()-[]{};:'"\,<>./?@#$%^&*_~''' ))
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punct = ""
for char in tes:
   if char not in punctuations:
       no_punct = no_punct + char     

print(punctuations(str))           
#"""



