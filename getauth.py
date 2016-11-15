import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

API = tweepy.API(auth)

print(API.me().name, "online and ready!")
# API.update_status(status="Checking OAuth authentication with tweepy...")
