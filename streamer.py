import tweepy
import logging


class TwitterStream(tweepy.StreamListener):

    def __init__(self, producer):
        """Requires a Kafka producer to send to Kafka each tweet in the stream"""
        tweepy.StreamListener.__init__(self)
        self.producer = producer

    def on_status(self, status):
        """Once the tweet has been read, it is sent to the Kafka topic"""
        # if "retweeted_status" attribute exists, flag this tweet as a retweet.
        is_retweet = hasattr(status, "retweeted_status")

        # check if text has been truncated
        if hasattr(status, "extended_tweet"):
            text = status.extended_tweet["full_text"]
        else:
            text = status.text

        if not is_retweet:
            self.producer.send(topic="timeline_tweets", value=text)

    def on_error(self, status_code):
        """If there's an error reading a tweet."""
        logging.error(f"Encountered streaming error ({status_code})")
        # Returned when an app is being rate limited for making too many requests.
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False
