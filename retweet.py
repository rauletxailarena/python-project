import tweepy
from time import sleep
from credentials import *

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



# iterate over tweets with #ocean, limit to 10
def tweet_example():
    for tweet in tweepy.Cursor(api.search, q='#ocean').items(10):
        try:
            print("\nTweet by: @" + tweet.user.screen_name)

            tweet = "@{} Ey! how is it going?".format(tweet.user.screen_name)

            api.update_status(tweet)

            sleep(5)
        except tweepy.TweepError as e:
            print (e.reason)
        except StopIteration:
            break


tweets = get_tweets()
print(len(tweets))








# Another way to query tweets:
# for tweet in tweepy.Cursor(api.search,
#                            q='#ocean',
#                            since='2016-11-25',
#                            until='2016-11-27',
#                            geocode='1.3552217,103.8231561,100km',
#                            lang='fr').items(10):
#     print('Tweet by: @' + tweet.user.screen_name)
