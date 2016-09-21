import tweepy
import Tweet
from afinn import Afinn


class MineListener(tweepy.StreamListener):
    tweets = []

    def on_status(self, status):

        print "Got a tweet..."
        tweet_id = status.id
        text = status.text
        retweet_count = status.retweet_count
        quotes_count = "--not implemented--"  # HOW to get this?
        favorited = status.favorited
        favorites_count = status.favorite_count  # Whether or not tweet was favorited rather than number of favorites
        author = status.author
        is_news = "--not implemented--"  # DEFINE LIST OF VALID NEWS AUTHORS

        tweet = Tweet.Tweet(tweet_id=tweet_id, text=text, retweet_count=retweet_count,
                            quotes_count=quotes_count, favorited=favorited,favorites_count=favorites_count,
                            author=author, is_news=is_news)
        MineListener.tweets.append(tweet)

        if len(MineListener.tweets) >= 10:
            return False

    def on_error(self, status_code):
        if status_code == 420:
            return False  # Disconnects the stream
