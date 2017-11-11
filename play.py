from helpers.substitutions import *
from helpers.tweepy_helper import *
from helpers.substitution_helper import *


for account in news_accounts:
    tweets = get_tweets_by_user(account, 1)
    print("tweet by: ", tweets[0].user.screen_name)
    print("tweet content: ", tweets[0].text)
