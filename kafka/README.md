
# Kafka Python Scripts

This repository contains a collection of small Python scripts for working with Apache Kafka. These scripts demonstrate basic Kafka operations, such as producing and consuming messages, and are intended for educational and testing purposes.

## Prerequisites

- Apache Kafka: Download and extract the Kafka binary distribution.
- Python 3.6 or later
- `kafka-python` package

## Installation

1. **Set up Kafka**  
   Open a new terminal and navigate to the Kafka directory:
   ```bash
   cd kafka_2.13-3.8.0
   ```

2. **Install `kafka-python`**  
   Install the `kafka-python` package by running the following command:
   ```bash
   pip3 install kafka-python
   ```

## Kafka Configuration and Setup

1. **Change to the Kafka Directory**  
   Navigate to the Kafka directory:
   ```bash
   cd kafka_2.13-3.8.0
   ```

2. **Generate a Cluster UUID**  
   Generate a unique Cluster UUID for the Kafka cluster:
   ```bash
   KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
   ```
   *Note: This cluster ID will be used by the KRaft controller.*

3. **Configure Log Directories**  
   KRaft requires the log directories to be configured. Run the following command to set up the log directories, passing the cluster ID:
   ```bash
   bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties
   ```

4. **Start the Kafka Server**  
   Now that KRaft is configured, start the Kafka server with the following command:
   ```bash
   bin/kafka-server-start.sh config/kraft/server.properties
   ```

## Usage

Once the setup is complete, you can run the Python scripts to interact with Kafka.

1. **Producer Script**  
   Run the producer script to send messages to a Kafka topic.
   ```bash
   python3 producer.py
   ```
   
2. **Consumer Script**  
   Run the consumer script to consume messages from a Kafka topic.
   ```bash
   python3 consumer.py
   ```

*Ensure Kafka is running before executing the scripts.*

## License

This project is provided for educational purposes and is not intended for production use.
