import os
import tweepy 
  
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

# update the status 
def postTweet():
  api.update_status(status ="Hello Everyone !") 
