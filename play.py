from helpers.substitutions import *
from helpers.tweepy_helper import *
from helpers.substitution_helper import *

tweets = get_most_used_words_from_news_accounts(10)

ranking = get_ranking(tweets)

print_ordered_ranking(ranking)
