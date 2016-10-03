import tweepy
import Tweet


class CursorListener():
    def __init__(self, query, twitter_api, max_limit=10):
        self.stock_query = query
        self.max_limit = max_limit
        self.twitter_api = twitter_api
        self.csv_path = ""

    def write_tweets(self):

        print "Getting tweets"

        searched_tweets = [status for status in
                           tweepy.Cursor(self.twitter_api.search, q=self.stock_query).items(self.max_limit)]
        for status in searched_tweets:

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

            # Writes the processed info to the file at csv_path
            tweet.writeDataToCsv(self.csv_path)
