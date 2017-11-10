import tweepy

# Consume:
consumer_key= 'Xu9KpEM4Kj40mnoOknMODq55J'
consumer_secret= 'XgdOvVdyVneYtCjkFsgVJZHxW5EtsbFCblI4qzUZLTxKJh7zmI'

# Access:
access_token= '11370472-GvDcmmZ7LdvOemUXVVNb3bQ6vpQ0axsEAQ9jgckA5'
access_token_secret = 'CJaL2trLh73KryXusAZeM2jyYV2AanTY0qbGcr7gDauhi'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet = "Hello world!"
api.update_status(status=tweet)
