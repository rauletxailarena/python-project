import tweepy
from time import sleep
from helpers.credentials import *
from sentiment_analysis import *
from textblob import TextBlob

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


###################################################################


news_accounts = ["BreakingNews", "BBCBreaking", "cnnbrk", "WSJbreakingnews", "ReutersLive",
"CBSTopNews", "AJELive", "SkyNewsBreak", "ABCNewsLive", "TWCBreaking"]


def get_tweets():
    result = []
    for account_name in news_accounts:
        tweets = (api.user_timeline(screen_name="BreakingNews", count=10))
        for tweet in tweets:
            result.append(tweet)
    return result
#



def get_tweets_by_hashtag(hashtag, number_of_tweets):
    result = []
    for tweet in tweepy.Cursor(api.search, q=hashtag).items(number_of_tweets):
        try:
            print("\nTweet by: @" + tweet.user.screen_name)
            result.append(tweet)
            # sleep(5)
        except tweepy.TweepError as e:
            print (e.reason)
        except StopIteration:
            break
    return result
#

def get_tweets_by_user(username, number_of_tweets):

    result = []
    tweets = (api.user_timeline(screen_name=username, count=number_of_tweets))
    for tweet in tweets:
        result.append(tweet)
    return result
#

tweets = get_tweets_by_user("@googlenews", 10)

list_of_tweets = []
for tweet in tweets:
    list_of_tweets.append(tweet.text)
print(list_of_tweets)












# Another way to query tweets:
# for tweet in tweepy.Cursor(api.search,
#                            q='#ocean',
#                            since='2016-11-25',
#                            until='2016-11-27',
#                            geocode='1.3552217,103.8231561,100km',
#                            lang='fr').items(10):
#     print('Tweet by: @' + tweet.user.screen_name)
