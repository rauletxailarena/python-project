# Import our Twitter credentials from credentials.py
from credentials import *
import tweepy
from time import sleep


# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open text file verne.txt (or your chosen file) for treading
my_file = open('verne.txt', 'r')

# Read lines one by one from my_file and assign to file_lines variable
file_lines = my_file.readlines()

# Close the file
my_file.close()

def tweet():

    # Iterate over file_lines
    for line in file_lines:
        try:
            print(line)
            if (line != '\n'):
                api.update_status(line)
                sleep(900)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)

# tweet()
