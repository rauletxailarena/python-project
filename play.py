from helpers.substitutions import *
from helpers.tweepy_helper import *
from helpers.substitution_helper import *



phrase = "The Drone that fell onto the Cars confirmed that the Poll station was poisoned"
phrase2 = "jaslfans a sfas flas faslf asf as"


lists_of_tweets = get_tweets_from_news_accounts(5)
print(get_most_used_words_from_news_accounts(2))
# print(len(lists_of_tweets))
