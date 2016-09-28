import traceback
import tweepy
import json

ckey = "4pHc0vgFVyHrAmQcbnD6Q8o7n"
csecret = "27uoBbX2qBKwqG1an5JZb1pijhj9RK404vfrWUwpc37PxfoXYJ"
atoken = "779415907428929537-AImQRy2jyrN3liiVCkUa9Me3ZmbCvWn"
asecret = "kDMEwV2WWBDfOhQnMWkteG0BOmJ4y1RCmYA3aO0xxdbPc"

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken, asecret)

#Reference to the data: https://dev.twitter.com/overview/api/tweets
def filteredData(jsonData):
	li = ["id","text","user","retweet_count", "quoted_status_id", "favorite_count", "followers_count","Sentiment","# of capitals","# of exclamation","# of question marks", "# emoticons"]
	#open method from StreamListener imported api.py and os (operating system interface) and create stock.csv file with default 0777 (security permission) and streaming data append onto the file and saved as relative path.
	cols = []
	for col in li:
		cols.append(str(jsonData[col]))
	filteredTweet = ",".join(cols)
	print type(filteredTweet)
	output = open('stock.csv','a')
	output.write(dicts)
	output.close()	


class listener(tweepy.StreamListener):
	def on_data(self, data):
		try:
			jsonData = json.loads(data)
			filteredData(jsonData)
			#return false if you wish to stop stream and close connection
			return True
		except BaseException, e:
			print 'failed ondata,',str(e)
			traceback.print_exc()
	def on_error(self,status):
		print status
#for information on difference between streaming and RESTful: https://dev.twitter.com/streaming/overview
twitterStream = tweepy.Stream(auth, listener())
twitterStream.filter(track=["stock"])

	
		
