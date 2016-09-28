import tweepy
import Tweet


class MineListener(tweepy.StreamListener):

    def __init__(self, tweet_limit=0, api=None):
        super(MineListener, self).__init__()
        self.csv_path = ''
        self.TWEET_LIMIT = tweet_limit
        self.tweet_count = 0

    def on_status(self, status):

        print "Got a tweet..."

        if self.TWEET_LIMIT == 0 or self.tweet_count < self.TWEET_LIMIT: #Can add a condition for saving a tweet 
            print "Accepted!"
            tweet_id = status.id
            text = status.text.encode("UTF-8")
            retweet_count = status.retweet_count
            quotes_count = "--not implemented--"  # HOW to get this?
            favorites_count = status.favorite_count
            author = status.author
            is_news = "--not implemented--"  # DEFINE LIST OF VALID NEWS AUTHORS
            timestamp = status.created_at

            #Instantiate tweet object, which processes the info 
            tweet = Tweet.Tweet(tweet_id=tweet_id, text=text, retweet_count=retweet_count,
                                quotes_count=quotes_count, favorites_count=favorites_count,
                                author=author, is_news=is_news, timestamp = timestamp)


            #Sets the path of csv file to first timestamp we gather
            if self.csv_path == '':
                self.csv_path = str(tweet.timestamp) + '.csv'
                print "Writing data to: "+self.csv_path
                tweet.writeHeaderToCsv(self.csv_path)

            #Writes the processed info to the file at csv_path
            tweet.writeDataToCsv(self.csv_path)

            self.tweet_count += 1

        else:
            print "Rejected.  Disconnecting..."
            print "Data written to file: "+self.csv_path
            return False

    def on_error(self, status_code):
        """
        This method will disconnect the stream if you have hit your 
        Twitter API connect limit.  This may be helpful as multiple failed 
        attempts at reconnecting causes longer timeouts.
        """ 
        if status_code == 420: #Hit twitter API streaming data limit
            return False  # Disconnects the stream
