import logging
from kafka import KafkaConsumer, KafkaProducer
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

    producer = KafkaProducer(bootstrap_servers="localhost:9092", compression_type="gzip",
                             value_serializer=lambda x:
                             json.dumps(x).encode('utf-8')
                             )

    for msg in consumer:
        tweet_dict = json.loads(json.dumps(msg.value))
        # check if text has been truncated
        if "extended_tweet" in tweet_dict:
            text = tweet_dict["extended_tweet"]["full_text"]
        else:
            text = tweet_dict["text"]
        # truncate so HF can process it.
        text = text[:500]
        date = tweet_dict["created_at"]
        hf_sentiment = classifier(text)[0]
        sentiment_pred = hf_sentiment['label']
        sentiment_score = hf_sentiment['score']
        hf_topic = topic_classifier(text, TOPICS)
        topic_pred = hf_topic['labels'][0]
        topic_score = hf_topic['scores'][0]
        data = {
            "date": date,
            "text": text,
            "sentiment_pred": sentiment_pred,
            "sentiment_score": sentiment_score,
            "topic_pred": topic_pred,
            "topic_score": topic_score
        }
        jsonified_data = json.dumps(data)
        logging.info((type(jsonified_data), jsonified_data))
        producer.send(topic="analyzed_data", value=jsonified_data)

