from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.empty import EmptyOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="Netflix_Data_Analytics",
    default_args=default_args,
    description="This DAG runs data analytics on top of Netflix datasets",
    start_date=datetime(2023, 5, 12),
    schedule=timedelta(days=1),
    catchup=False,
    tags=["netflix", "tutorial"],
) as dag:

    start_task = EmptyOperator(task_id="start_task")
    end_task = EmptyOperator(task_id="end_task")

    start_task >> end_task