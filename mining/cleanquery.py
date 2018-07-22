query = "query-filter:retweets"

def cleanquery():    
    if "-filter:retweets" in query:
        print(query[:-16])