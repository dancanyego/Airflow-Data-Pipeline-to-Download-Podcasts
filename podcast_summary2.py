import airflow.decorators
import pendulum
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.sqlite.hooks.sqlite import SqliteHook

# Define the default arguments
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': pendulum.duration(minutes=5),
}

# Define the DAG
@airflow.decorators.dag(
    dag_id = "podcast_summary2",
    schedule_interval='@daily',
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    default_args=default_args,
    description='A podcast dag',
)
def podcast_summary2():
    pass

# Instantiate the DAG 
summary = podcast_summary2()
