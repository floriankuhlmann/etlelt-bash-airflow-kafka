#### Some usefull commands to run kafka via commandline

Download Kafka, extract and prepare
```bash
wget https://downloads.apache.org/kafka/3.8.0/kafka_2.13-3.8.0.tgz
tar -xzf kafka_2.13-3.8.0.tgz
cd kafka_2.13-3.8.0
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
```

configure the log directories passing the cluster ID.
```bash
bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties
```

start the Kafka server by running the following command.
```bash
bin/kafka-server-start.sh config/kraft/server.properties
```

create a topic named news
```bash
bin/kafka-topics.sh --create --topic news --bootstrap-server localhost
```

start a producer
```bash
bin/kafka-console-producer.sh   --bootstrap-server localhost:9092   --topic news
```

listen to the messages in the topic news
```bash
bin/kafka-console-consumer.sh   --bootstrap-server localhost:9092   --topic news   --from-beginning
```