from afinn import Afinn

class Tweet:

	def countCapitals(self, text):
		count = 0
		for char in text:
			if char.isupper():
				count+= 1
		return count

	def countQuestionMarks(self, text):
		count = 0
		for char in text:
			if char == '?':
				count+= 1
		return count

	def countExclamationMarks(self, text):
		count = 0
		for char in text:
			if char == '!':
				count += 1
		return count

	def countEmoticons(self, text):
		pass


#Derive: SENTIMENT, CAPITALS, QUESTION MARKS, EMOTICONS
	def __init__(self, tweet_id, text, author, retweet_count, quotes_count, favorites_count, is_news):
		self.tweet_id = tweet_id
		self.text = text
		self.author = author
		self.retweet_count = retweet_count
		self.quotes_count = quotes_count
		self.favorites_count = favorites_count
		self.is_news = is_news
		
		afinn = Afinn()
		self.verified = self.author.verified
		self.follower_count = self.author.followers_count
		self.sentiment = afinn.score(text)
		self.capitals = self.countCapitals(text)
		self.exclamationmarks = self.countExclamationMarks(text)
		self.questionmarks = self.countQuestionMarks(text)
		#self.emoticons


	def printData(self):
		print 'tweet_id: '+str(self.tweet_id)
		print '---TEXT---'
		print self.text
		print '---END---'
		print 'is_news: '+str(self.is_news)
		print 'verified: '+str(self.verified)
		print 'retweet_count: '+str(self.retweet_count)
		print 'quotes_count: '+str(self.quotes_count)
		#print 'favorites_count: '+str(self.favorites_count)  DONT KNOW HOW TO COUNT FAVORITES
		print 'favorited: '+str(self.favorites_count)
		print 'followers_count: '+str(self.follower_count)
		print 'capitals: '+str(self.capitals)
		print 'questionmarks: '+str(self.questionmarks)
		print 'exclamationmarks: '+str(self.exclamationmarks)
		print 'sentiment: '+str(self.sentiment)
