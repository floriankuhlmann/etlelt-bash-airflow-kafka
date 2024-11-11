#### Some usefull commands to run airflow via commandline

list all the existing DAGs.
```bash
airflow dags list
```

Verify that my-first-python-etl-dag is a part of the output.
```bash
airflow dags list | grep "my-first-python-etl-dag"
```

list all tasks in the DAG named example_bash_operator.
```bash
airflow tasks list example_bash_operator
```

If you don't find your DAG in the list, you can check for errors using the following command
```bash
airflow dags list-import-errors
```

unpause a DAG named tutorial
```bash
airflow dags unpause tutorial
```

unpause a DAG named tutorial
```bash
airflow dags pause tutorial
```

set the AIRFLOW_HOME
```bash
export AIRFLOW_HOME=/home/project/airflow
echo $AIRFLOW_HOME
```

submit by just copying the DAG to the corresponding dag dir
```bash
 cp example_dag.py $AIRFLOW_HOME/dags
```

