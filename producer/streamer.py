import tweepy
import logging


class TwitterStream(tweepy.StreamListener):

    def __init__(self, producer):
        """Requires a Kafka producer to send to Kafka each tweet in the stream"""
        tweepy.StreamListener.__init__(self)
        self.producer = producer

    def on_status(self, status):
        """Once the tweet has been read, it is sent to the Kafka topic"""
        self.producer.send(topic="timeline_tweets", value=status._json)

    def on_error(self, status_code):
        """If there's an error reading a tweet."""
        logging.error(f"Encountered streaming error ({status_code})")
        # Returned when an app is being rate limited for making too many requests.
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False
