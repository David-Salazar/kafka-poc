# %%
from tweets_reader import get_twitter_api
from kafka import KafkaProducer
from json import dumps
from streamer import TwitterStream
import logging
import tweepy

if __name__ == "__main__":
    # authenticate and access Twitter API
    api = get_twitter_api()
    logging.info("Authenticated on twitter")
    # create Kafka producer
    # improve performance by compressing the messages sent to Kafka
    producer = KafkaProducer(bootstrap_servers="localhost:9092", compression_type="gzip",
                             value_serializer=lambda x:
                             dumps(x).encode('utf-8')
                             )
    myStreamListener = TwitterStream(producer)
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=["Bitcoin"])
    myStreamListener.producer.close()
