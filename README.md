
# ETL and Data Pipelines with Shell, Airflow, and Kafka

This repository contains scripts and example DAGs related to the Coursera course "[ETL and Data Pipelines with Shell, Airflow, and Kafka](https://www.coursera.org/learn/etl-and-data-pipelines-shell-airflow-kafka/)." The course provides an introduction to two approaches for converting raw data into analytics-ready data: the ETL (Extract, Transform, Load) process and the ELT (Extract, Load, Transform) process. These processes are used in data warehouses, data marts, and data lakes, respectively, and involve transforming, loading, and storing data from source systems to destination systems.

## Course Overview

In this course, learners explore tools and techniques for building ETL and ELT data pipelines. Key concepts covered include:

- Differences between ETL and ELT processes and their use cases
- Methods and tools for extracting, transforming, and loading data
- Data quality verification, monitoring of load failures, and recovery mechanisms
- Building data pipelines with Apache Airflow
- Creating streaming pipelines with Apache Kafka, covering brokers, topics, partitions, replications, producers, and consumers

## Repository Structure

The repository is organized as follows:

- **`bash/`**: Contains Bash scripts with useful commands for ETL processes. These scripts can be used to manage and monitor ETL workflows via the command line.

  - **`airflow_cmd.md`**: Provides various commands for managing Apache Airflow tasks from the command line, such as listing DAGs, pausing/unpausing tasks, and setting the `AIRFLOW_HOME` environment variable.
  - **`bash_cmd.md`**: Includes additional Bash commands useful in ETL workflows.
  
- **`dag/`**: Contains example DAG (Directed Acyclic Graph) files for Apache Airflow. These DAGs illustrate the structure of an Airflow pipeline and demonstrate basic ETL processes.

  - **`example_dag.py`**: A sample DAG that can be used as a starting point for creating ETL workflows.
  - **`example_server_access_log_processing.py`**: Another sample DAG that may include tasks for processing server access logs.

## Getting Started

1. **Set up Airflow**: Follow the Airflow installation guide to set up your environment. Ensure that the `AIRFLOW_HOME` environment variable is correctly configured.
2. **Run Commands**: Refer to the `airflow_cmd.md` and `bash_cmd.md` files in the `bash/` folder for useful commands to manage DAGs and perform ETL tasks.
3. **Copy DAGs**: To use an example DAG, copy the file to your Airflow DAG directory (as defined by the `AIRFLOW_HOME` environment variable).

Example:
   ```bash
   cp dag/example_dag.py $AIRFLOW_HOME/dags
   ```

## Requirements

- **Apache Airflow**: Required to run the DAGs and manage ETL workflows.
- **Apache Kafka**: Useful for implementing streaming pipelines if applicable.
- **Bash**: The Bash commands are meant to be executed in a Unix-based environment.

## License

This project is intended for educational purposes in line with the Coursera course and is not meant for production use.
