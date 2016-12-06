import tweepy

class CursorListener():
    def __init__(self, topic, tweepy_api, max_limit=10):
        self.topic = topic
        self.tweepy_api = tweepy_api
        self.max_limit=10
        self.csv_path = ""
        
    def getTweets(self):
        searched = [status for status in tweepy.Cursor(self.tweepy_api.search, q=self.topic).items(self.max_limit)]

        collected = {}
        for status in searched:

            tweet_id = status.id
            text = repr(status.text)
            retweet_count = status.retweet_count
            quotes_count = "--not implemented--"  # HOW to get this?
            favorites_count = status.favorite_count
            author = status.author
            is_news = "--not implemented--"  # DEFINE LIST OF VALID NEWS AUTHORS
            timestamp = status.created_at

            # Instantiate tweet object, which processes the info
            tweet = Tweet.Tweet(tweet_id=tweet_id, text=text, retweet_count=retweet_count,
                                quotes_count=quotes_count, favorites_count=favorites_count,
                                author=author, is_news=is_news, timestamp=timestamp)

            # Sets the path of csv file to first timestamp we gather
            if self.csv_path == "":
                self.csv_path = str(self.stock_query[1:]) + str(tweet.timestamp) + ".csv"
                print "Writing data to: " + self.csv_path
                tweet.writeHeaderToCsv(self.csv_path)

            #hashmap for duplicating tweets
            if tweet.tweet_id not in collected.keys():
                collected[tweet.tweet_id] = tweet

        # Writes the processed info to the file at csv_path
        for tweet_id in collected.keys():
            collected[tweet_id].writeDataToCsv(self.csv_path)

        return collected

        
