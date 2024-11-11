# import the libraries
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# Set default arguments
default_args = {
    'owner': 'Florian Kuhlmann',
    'start_date': days_ago(0),
    'email': ['fk@somemail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    dag_id='ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(days=1),
)

# Define the tasks
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar xvf tolldata.tgz -C ',
    dag=dag,
)

extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -d"," -f1,2,3,4 vehicle-data.csv > csv_data.csv',
    dag=dag,
)

extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command="cut -d$'\t' -f5,6,7 tollplaza-data.tsv | tr '\t' ',' | tr -d '\t' > tsv_data.csv",
    dag=dag
)

# Task to clean fixed_width_data.csv
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command="awk '{print $10 \",\" $11}' payment-data.txt | tr -d '\t' > fixed_width_data.csv",
    dag=dag
)

consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command='paste -d "," csv_data.csv tsv_data.csv fixed_width_data.csv > extracted_data.csv',
    dag=dag,
)

# Sixth task: Transform data by capitalizing the vehicle_type column
transform_data = BashOperator(
    task_id='transform_data',
    bash_command=(
        "cut -d, -f1-3 extracted_data.csv | tr -d '\t' > columns1-4.csv; "
        "cut -d, -f4 extracted_data.csv | tr 'a-z' 'A-Z' > vehicle_type_upper.csv; "
        "cut -d, -f5-9 extracted_data.csv | tr -d '\t' > columns6-10.csv; "            
        "paste -d, columns1-4.csv vehicle_type_upper.csv columns6-10.csv | tr '\t' ',' > transformed_data.csv"
    ),
)

# Define task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data