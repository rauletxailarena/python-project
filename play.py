from helpers.substitutions import *
from helpers.tweepy_helper import *
from helpers.substitution_helper import *

a = get_tweets_by_news_accounts(1)

for list_of_tweets in a:
    for tweet in list_of_tweets:
        print(tweet.text)
