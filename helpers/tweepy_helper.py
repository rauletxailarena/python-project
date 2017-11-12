import tweepy
from time import sleep
from helpers.credentials import *
from helpers.sentiment_analysis_helper import *
from textblob import TextBlob
from helpers.news_accounts import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



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

def get_tweets_from_news_accounts(number_of_tweets):
    result = []
    for account in news_accounts:
        print("Getting tweets from ", account)
        result.append(get_tweets_by_user(account, number_of_tweets))
    flat_result = []
    for list_of_tweets in result:
        for item in list_of_tweets:
            flat_result.append(item)
    return flat_result


# Another way to query tweets:
# for tweet in tweepy.Cursor(api.search,
#                            q='#ocean',
#                            since='2016-11-25',
#                            until='2016-11-27',
#                            geocode='1.3552217,103.8231561,100km',
#                            lang='fr').items(10):
#     print('Tweet by: @' + tweet.user.screen_name)
