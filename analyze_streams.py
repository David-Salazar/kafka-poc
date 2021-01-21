import logging
from kafka import KafkaConsumer
import json
from transformers import pipeline

if __name__ == "__main__":
    classifier = pipeline('sentiment-analysis')
    topic_classifier = pipeline("zero-shot-classification")
    TOPICS = ['the economy', 'education', 'commerce', 'politics', 'public health', 'vaccines', 'conspiracy',
              'sports events', 'comedy', 'mental health', 'death', 'disease', 'natural environment', 'globalization',
              'China']
    consumer = KafkaConsumer('timeline_tweets', bootstrap_servers='localhost:9092',
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for msg in consumer:
        tweet_dict = json.loads(json.dumps(msg.value))
        # check if text has been truncated
        if "extended_tweet" in tweet_dict:
            text = tweet_dict["extended_tweet"]["full_text"]
        else:
            text = tweet_dict["text"]
        # truncate so HF can process it.
        text = text[:500]
        time = tweet_dict["created_at"]
        hf_sentiment = classifier(text)[0]
        sentiment_pred = hf_sentiment['label']
        sentiment_score = hf_sentiment['score']
        hf_topic = topic_classifier(text, TOPICS)
        topic_pred = hf_topic['labels'][0]
        topic_score = hf_topic['scores'][0]
        print(text, sentiment_pred, sentiment_score, topic_pred, topic_score)


