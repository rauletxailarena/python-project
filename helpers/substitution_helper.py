from helpers.substitutions import *
from helpers.tweepy_helper import *

def substitute_word(word):
    return substitutions[word]


def contains_keyword(phrase):
    phrase = phrase.split()
    for word in phrase:
        word = word.lower()
        if (word in substitutions):
            return True
    else:
        return False


def is_keyword(word):
    word = word.lower()
    if (word in substitutions):
        return True
    else:
        return False

def substitute_keywords(phrase):
    if contains_keyword(phrase):
        new_phrase = ""
        phrase = phrase.split()
        for word in phrase:
            if is_keyword(word):
                new_phrase += " "
                new_phrase += substitutions[word]
            else:
                new_phrase += " "
                new_phrase += word
        return new_phrase

def get_sustitutability_index(phrase):
    index = 0
    phrase = phrase.split()
    for word in phrase:
        if is_keyword(word):
            index += 1
    return index

def get_most_used_words(list_of_phrases):
    result = {}
    for phrase in list_of_phrases:
        phrase = phrase.split()
        for word in phrase:
            word = word.lower()
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
    return result

def get_most_used_words_from_news_accounts(number_of_tweets):
    tweets = get_tweets_from_news_accounts(number_of_tweets)
    tweets_text = [clean_tweet(tweet.text) for tweet in tweets]
    result = get_most_used_words(tweets_text)
    return result
