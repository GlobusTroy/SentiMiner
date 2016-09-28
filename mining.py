import tweepy
from MiningListener import MineListener
import time

#TODO: Read from the file instead of hardcoding?
def getAuthenticatedAPI():
	auth = tweepy.OAuthHandler('WuOEiRzGJzlHt1H2imTCPUpfR','X47THIKVxHqGxdHv8AkrcwyU3bH1NW91gIBang8mamhGim7n2Z')
	auth.set_access_token('778344887867416576-jKrxd6xzfdCispj9HTPpN4DEZwkkIJV', 'vgLsPQLtoRaIqfJjaRd7jLUvVMyhazYsrYhvLucjv9Q5r')

	#Can add paramaters wait_on_rate_limit and wait_on_rate_limit_notify to api object.
	api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
	return api


api = getAuthenticatedAPI()

#No tweet_limit parameter means no limit, otherwise add
#Minelistener(tweet_limit = x) to stop after x tweets
listener = MineListener()

#Create stream object
stream = tweepy.Stream(auth = api.auth, listener = listener)

#Get stream running //  Put keywords here
stream.filter(track = ["party"])


