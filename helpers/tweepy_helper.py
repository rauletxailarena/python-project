import tweepy
from time import sleep
from helpers.credentials import *
from helpers.sentiment_analysis_helper import *
from textblob import TextBlob
from helpers.news_accounts import *
from helpers.substitution_helper import *

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

## Returns a flat list of tweets
def get_tweets_from_news_accounts(number_of_tweets):
    result = []
    for account in long_news_accounts:
        print("Getting tweets from ", account)
        result.append(get_tweets_by_user(account, number_of_tweets))
    flat_result = []
    for list_of_tweets in result:
        for item in list_of_tweets:
            flat_result.append(item)
    return flat_result

def tweet_helper(list_of_tweets):
    current_index = 0
    for tweet in list_of_tweets:
        try:
            api.update_status(list_of_tweets[current_index])
            break
        except:
            print("An error occured. Moving onto the next tweet")
            current_index += 1
# Another way to query tweets:
# for tweet in tweepy.Cursor(api.search,
#                            q='#ocean',
#                            since='2016-11-25',
#                            until='2016-11-27',
#                            geocode='1.3552217,103.8231561,100km',
#                            lang='fr').items(10):
#     print('Tweet by: @' + tweet.user.screen_name)


def run():
    list_of_tweets =  get_tweets_from_news_accounts(10)
    list_of_tweet_text = []
    for tweet in list_of_tweets:
        list_of_tweet_text.append(tweet.text)
    tweet_ranking = create_tweet_ranking(list_of_tweets)
    ordered_list_of_tweets = get_ordered_list_with_most_substitutable_tweets(tweet_ranking)
    adapted_tweets = []
    for tweet in ordered_list_of_tweets:
        adapted_tweets.append(substitute_keywords(tweet))
    return adapted_tweets
