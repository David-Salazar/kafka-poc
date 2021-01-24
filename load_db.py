from kafka import KafkaConsumer
import json
import pymysql
import datetime

ENDPOINT = "database-kaka.c8wdpocz3thc.us-east-1.rds.amazonaws.com"
PASSWORD = "Bf2TiD4M4aOpbglEd9lM"
DBNAME = "databasekafka"
USR = "admin"
PORT = 3306

if __name__ == '__main__':
    consumer = KafkaConsumer('analyzed_data', bootstrap_servers='localhost:9092',
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    connection = pymysql.connect(host=ENDPOINT, user=USR, password=PASSWORD, port=PORT, db=DBNAME)
    SQL = """INSERT INTO covid_tweets 
    (tweet, date_creation, sentiment_prediction, sentiment_score, topic_prediction, topic_score)
    VALUES (%s, %s, %s, %s, %s, %s)"""
    for msg in consumer:
        data = json.loads(msg.value)
        date = data["date"]
        date = datetime.datetime.strptime(date, "%a %b %d %H:%M:%S %z %Y").strftime("%Y-%m-%d %H:%M:%S")
        text = data["text"]
        sentiment_pred = data["sentiment_pred"]
        sentiment_score = data["sentiment_score"]
        topic_pred = data["topic_pred"]
        topic_score = data["topic_score"]
        with connection.cursor() as cursor:
            cursor.execute(SQL, (text, date, sentiment_pred, sentiment_score, topic_pred, topic_score))
        connection.commit()
    connection.close()