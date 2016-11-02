from afinn import Afinn
import csv


class Tweet:
    def countCapitals(self, text):
        count = 0
        for char in text:
            if char.isupper():
                count += 1
        return count

    def countQuestionMarks(self, text):
        count = 0
        for char in text:
            if char == '?':
                count += 1
        return count

    def countExclamationMarks(self, text):
        count = 0
        for char in text:
            if char == '!':
                count += 1
        return count


    # Derive: SENTIMENT, CAPITALS, QUESTION MARKS, EMOTICONS
    def __init__(self, tweet_id, text, author, retweet_count, quotes_count, favorites_count, is_news, timestamp):
        self.tweet_id = tweet_id
        self.text = text
        self.text_char_list = text.split(" ")  # split to get emojis as UTF-8 encoding
        self.author = author
        self.retweet_count = retweet_count
        self.quotes_count = quotes_count
        self.favorites_count = favorites_count
        self.is_news = is_news
        self.timestamp = timestamp

        afinn = Afinn(emoticons=True)
        self.sentiment = afinn.score(text)
        self.verified = self.author.verified
        self.follower_count = self.author.followers_count
        self.capitals = self.countCapitals(text)
        self.exclamation_marks = self.countExclamationMarks(text)
        self.question_marks = self.countQuestionMarks(text)

    def printData(self):
        print 'tweet_id: ' + str(self.tweet_id)
        print '---TEXT---'
        print self.text
        print '---END---'
        print 'is_news: ' + str(self.is_news)
        print 'verified: ' + str(self.verified)
        print 'retweet_count: ' + str(self.retweet_count)
        print 'quotes_count: ' + str(self.quotes_count)
        print 'favorites_count: ' + str(self.favorites_count)
        print 'followers_count: ' + str(self.follower_count)
        print 'capitals: ' + str(self.capitals)
        print 'question_marks: ' + str(self.question_marks)
        print 'exclamationmarks: ' + str(self.exclamation_marks)
        print 'sentiment: ' + str(self.sentiment)
        print 'timestamp: ' + str(self.timestamp)

    # I HAVE EXCLUDED "Quotes Count" AS I DO NOT SEE A WAY TO SCRAPE THAT INFO YET
    # Excluded is_news as that is not yet something we have a method to determine
    def getCsvList(self):
        """
        Returns the info into a list in this order:
        ID, text, isVerified, #retweets, #favorites, #followers, sentiment, #capitals, # of !, # of ?, #emoticons
        """
        return [self.tweet_id, self.text, self.verified, self.retweet_count,
                self.favorites_count, self.follower_count, self.sentiment, self.capitals,
                self.exclamation_marks, self.question_marks,self.timestamp]

    def getCsvHeader(self):
        return ['ID', 'Text', 'verified', 'retweet_count', 'favorites_count', 'follower_count',
                'sentiment', 'capitals', 'exclamation_marks', 'question_marks','timestamp']

    def writeHeaderToCsv(self, filename):
        with open('Tweet Data/'+filename, 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.getCsvHeader())

    # Appends to the end of the target CSV file, or else creates a new one
    def writeDataToCsv(self, filename):
        with open('Tweet Data/'+filename, 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.getCsvList())
