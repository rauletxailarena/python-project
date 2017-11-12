from helpers.substitutions import *
from helpers.tweepy_helper import *


def substitute_keywords(phrase):
    new_phrase = phrase
    for key in substitutions:
        if key in phrase:
            print("key " + key + " found in " + phrase)
            new_phrase = new_phrase.replace(key, substitutions[key])
            print("Changing word " +key + " for the word " + substitutions[key])
    return new_phrase

def contains_keyword(phrase):
    for key in substitutions:
        if key in phrase:
            return True
    return False

def minimize_words(phrase):
    new_phrase = ""
    phrase = phrase.split()
    for word in phrase:
        new_phrase += word.lower() + " "
    return new_phrase


def get_sustitutability_index(phrase):
    index = 0
    phrase = minimize_words(phrase)
    for key in substitutions:
        if key in phrase:
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
