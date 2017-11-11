from helpers.substitutions import *

def substitute_word(word):
    return substitutions[word]


def contains_keyword(phrase):
    phrase = phrase.split()
    for word in phrase:
        if (word in substitutions):
            return True
    else:
        return False


def is_keyword(word):
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
