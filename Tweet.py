from afinn import Afinn

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

    def countEmojis(self, char_list):
        emoji_ctr = 0
        for char in char_list:

            #convert character to utf-8
            char = repr(char)
            char = char[1:len(char)-1]

            #every emoji has the following utf-8 format: \\xf0\\x9f\\x98\\x
            lst = char.count('\\xf0\\x9f\\x98\\x')
            emoji_ctr += lst

        return emoji_ctr


    # Derive: SENTIMENT, CAPITALS, QUESTION MARKS, EMOTICONS
    def __init__(self, tweet_id, text, author, retweet_count, quotes_count, favorites_count, is_news):
        self.tweet_id = tweet_id
        self.text = text
        self.text_char_list = text.split(" ")  # split to get emojis as UTF-8 encoding
        self.author = author
        self.retweet_count = retweet_count
        self.quotes_count = quotes_count
        self.favorites_count = favorites_count
        self.is_news = is_news

        afinn = Afinn()
        self.sentiment = afinn.score(text)
        self.verified = self.author.verified
        self.follower_count = self.author.followers_count
        self.capitals = self.countCapitals(text)
        self.exclamation_marks = self.countExclamationMarks(text)
        self.question_marks = self.countQuestionMarks(text)
        self.emoticons = self.countEmojis(self.text_char_list)


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
        print 'emojis: '+str(self.emoticons)
