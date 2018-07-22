import datetime

#convert date format 01-15-2018 ke 2018-01-15 (format tweepy date)
def sinceDate(date):
    since = date[:10].replace('/', '-')
    since = datetime.datetime.strptime(since, '%m-%d-%Y').strftime('%Y-%m-%d')
    return since

def untilDate(date):
    until = date[13:].replace('/', '-')
    until = datetime.datetime.strptime(until, '%m-%d-%Y').strftime('%Y-%m-%d')
    return until

"""
test
d = "01/13/2018 - 01/15/2018"
sinceDate(d)
untilDate(d)
"""