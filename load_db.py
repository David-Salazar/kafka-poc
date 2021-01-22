from kafka import KafkaConsumer
import json


if __name__ == '__main__':
    consumer = KafkaConsumer('analyzed_data', bootstrap_servers='localhost:9092',
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for msg in consumer:
        data = json.loads(json.dumps(msg.value))
        print(data)