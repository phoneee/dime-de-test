from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from financial_etl import fetch_and_process_delisted, process_dividends_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'financial_data_processing',
    default_args=default_args,
    description='A simple DAG for financial data processing',
    schedule_interval=timedelta(days=1),
)

fetch_delisted_task = PythonOperator(
    task_id='fetch_and_process_delisted',
    python_callable=fetch_and_process_delisted,
    dag=dag,
)

process_dividends_task = PythonOperator(
    task_id='process_dividends_data',
    python_callable=process_dividends_data,
    dag=dag,
)

fetch_delisted_task >> process_dividends_task
