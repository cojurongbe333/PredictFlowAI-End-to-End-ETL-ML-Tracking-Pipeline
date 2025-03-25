
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import os

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

dag = DAG(
    'etl_support_usage_pipeline',
    default_args=default_args,
    description='ETL pipeline for support logs and usage data',
    schedule_interval='@daily',
    catchup=False
)

def extract_support():
    df = pd.read_csv('/opt/airflow/data/support_logs.csv')
    df.to_csv('/opt/airflow/data/interim/support_extracted.csv', index=False)

def extract_usage():
    df = pd.read_csv('/opt/airflow/data/product_usage.csv')
    df.to_csv('/opt/airflow/data/interim/usage_extracted.csv', index=False)

def transform_merge():
    support = pd.read_csv('/opt/airflow/data/interim/support_extracted.csv')
    usage = pd.read_csv('/opt/airflow/data/interim/usage_extracted.csv')
    merged = pd.merge(support, usage, on='user_id', how='left')
    merged.to_csv('/opt/airflow/data/processed/merged_logs.csv', index=False)

with dag:
    t1 = PythonOperator(task_id='extract_support', python_callable=extract_support)
    t2 = PythonOperator(task_id='extract_usage', python_callable=extract_usage)
    t3 = PythonOperator(task_id='transform_merge', python_callable=transform_merge)

    [t1, t2] >> t3
