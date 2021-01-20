import logging
from kafka import KafkaConsumer
from transformers import pipeline

if __name__ == "__main__":
    classifier = pipeline('sentiment-analysis')
    consumer = KafkaConsumer('timeline_tweets')
    for msg in consumer:
        tweet = msg.value.decode("utf-8")
        tweet = tweet[:500]
        print(tweet, classifier(tweet))
