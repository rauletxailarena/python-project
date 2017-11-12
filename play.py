from helpers.substitutions import *
from helpers.tweepy_helper import *
from helpers.substitution_helper import *


phrase1 = "This is a phrase"
phrase2 = "This is another phrase"

a = get_most_used_words([phrase1, phrase2])
print (a)
