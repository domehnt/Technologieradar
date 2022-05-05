import tweepy
from textblob import TextBlob
import config_token
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import psycopg2
from database_connection_config import config
from cleantext import clean


params_ = config()
conn = psycopg2.connect(**params_)
cur = conn.cursor()
conn.autocommit = True
params_ = config()

def getClient():
    client = tweepy.Client(bearer_token=config_token.BEARER_TOKEN)

    return client

def searchTweets(query):
    client = getClient()

    tweets = client.search_recent_tweets(query=query, max_results=100,)#tweet_fields=['context_annotations', 'created_at'],
                                                                    # media_fields=['preview_image_url'], expansions='attachments.media_keys',

    tweet_data = tweets.data
    results = []

    for tweet in tweet_data:
        if not tweet_data is None and len(tweet_data) > 0:
            results.append(tweet.text)
        else:
            return []



    return results


emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002500-\U00002BEF"  # chinese char
                           u"\U00002702-\U000027B0"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"\U0001f926-\U0001f937"
                           u"\U00010000-\U0010ffff"
                           u"\u2640-\u2642"
                           u"\u2600-\u2B55"
                           u"\u200d"
                           u"\u23cf"
                           u"\u23e9"
                           u"\u231a"
                           u"\ufe0f"  # dingbats
                           u"\u3030"
                           "]+", flags=re.UNICODE)


def cleanText (text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  #remove.substring mentions
    text = re.sub(r'#', '', text) #removing the # symbol
    text = re.sub(r'RT[\s]+', '', text) #remove RT
    text = re.sub(r'http\S+', '', text)  #remove hyper link'
    text = emoji_pattern.sub(r'', text)

    return text



def get_subjectivity(text):
    subjectivity = TextBlob(text).sentiment.subjectivity
    return subjectivity

def get_polarity(text):
    polarity = TextBlob(text).sentiment.polarity

    return polarity

query= "Bitcoin lang:en"
tweets = searchTweets(query)

String_text = '##ll=='.join(tweets)
String_text_1 = String_text.split('##ll==')
#print(String_text_1)
i = 1



for element in String_text_1:
    cleaning_tweet = cleanText(element)
    score_polarity = get_polarity(cleaning_tweet)
    score_subjectivity = get_subjectivity(cleaning_tweet)
    cur.execute("INSERT INTO Sentimentresults (orginaltweet, sentiment, subjectivity) "
                "VALUES(%s, %s, %s)", (cleaning_tweet, score_polarity, score_subjectivity,))

    print(str(i) + ') ' + cleaning_tweet )
    print("score_polarity: " + str(score_polarity) + "   -----   " + "score_subjectivity: " + str(score_subjectivity))
    if score_polarity < 0:
        print("Der Tweet ist negativ")
    elif score_polarity > 0:
        print("Der Tweet ist positiv")
    elif score_polarity == 0:
        print("Der Tweet ist neutral")
    print("\n")
    i += 1

cur.close()
conn.close()