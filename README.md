# Learning Apache Kafka

Apache Kafka is a high throughput distributed messaging system. This repository is  a POC creating a Producer that 
streams tweets from my own Twitter account in real time. 

# Running instructions

1. Put your own twitter authentication keys in the `twitter_oauth.ini` configuration file. 
2. `cd` into the folder containing the installation. Run the following commands in two terminals 
   (once you have Apache Kafka installed in your system). These commands create the zookeeper
   and kafka servers in your local computer

```
zookeeper-server-start config/zookeeper.properties
kafka-server-start config/server.properties
```
3. Create a Kafka topic to store the tweets:

```
 kafka-topics --bootstrap-server localhost:9092 --topic timeline_tweets --create --partitions 3
```

4. Create (only if this is your first time running the project) an Apache Kafka consumer in your terminal with the following command:

```
kafka-console-consumer --bootstrap-server localhost:9092 --topic timeline_tweets
```
5. Run `main.py`. It will read the tweets from your timeline, create a producer that reads into the topic you just
created and, finally, your CLI consumer will read these very same tweets. 
   
```
python producer.py
```

cd producer
docker image build -t kafka_producer .
docker container run --network="host" kafka_producer

cd ../stream_analysis
docker image build -t streams_analysis .
docker container run --network="host" streams_analysis

