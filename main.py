# %%
from tweets_reader import get_twitter_api
from kafka import KafkaProducer
from json import dumps

# authenticate and access Twitter API
api = get_twitter_api()
# read tweets from my timeline
public_tweets = api.home_timeline()

# create Kafka producer
# improve performance by compressing the messages sent to Kafka
producer = KafkaProducer(g="localhost:9092", compression_type="gzip",
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8')
                         )

for tweet in public_tweets:
    producer.send(topic="timeline_tweets", value=tweet.text)

producer.close()
