import tweepy
import Tweet


class MineListener(tweepy.StreamListener):
    tweets = []

    def on_status(self, status):

        print "Got a tweet..."

        if 1: #Add a condition for saving a tweet // Contains emoji, favorites, etc to test 
            print "Accepted!"
            tweet_id = status.id
            text = status.text.encode("UTF-8")
            retweet_count = status.retweet_count
            quotes_count = "--not implemented--"  # HOW to get this?
            favorites_count = status.favorite_count
            author = status.author
            is_news = "--not implemented--"  # DEFINE LIST OF VALID NEWS AUTHORS

            tweet = Tweet.Tweet(tweet_id=tweet_id, text=text, retweet_count=retweet_count,
                                quotes_count=quotes_count, favorites_count=favorites_count,
                                author=author, is_news=is_news)
            MineListener.tweets.append(tweet)
        else:
            print "Rejected..."


        if len(MineListener.tweets) >= 10:
            return False

    def on_error(self, status_code):
        if status_code == 420:
            return False  # Disconnects the stream
