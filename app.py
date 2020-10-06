import os
import tweepy
from get_data import pokemon_data
  
# twitter credentials
consumer_key = os.environ.get("api_key")
consumer_secret = os.environ.get("api_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_secret")

# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth) 

#pokemon data to post
name, ptp1, ptp2 = pokemon_data()
tweet_message = "Daily Pokedesk data: " + name + " type: " + ptp1 + " - " + ptp2 + " - published by python code -"

# update the status 
def postTweet():
  print("posting top:", os.environ.get("api_key"))
  api.update_status(status = tweet_message)
