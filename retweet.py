import tweepy
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# iterate over tweets with #ocean, limit to 10
for tweet in tweepy.Cursor(api.search, q='#ocean').items(10):
    # print the usernames of the last 10 people to use #ocean
    print("Tweet by: @" + tweet.user.screen_name)
