from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago
import json


## Define the DAG
with DAG(
    dag_id='nasa_apod_postgres',
    start_date=days_ago(1),
    schedule_interval='@daily',
    catchup=False

) as dag:
    
    ## step 1: Create the table if it doesnt exists

    @task
    def create_table():
        pass


    ## Step 2: Extract the NASA API Data(APOD)-Astronomy Picture of the Day[Extract pipeline]
    ## https://api.nasa.gov/planetary/apod?api_key=7BbRvxo8uuzas9U3ho1RwHQQCkZIZtJojRIr293q
    extract_apod=SimpleHttpOperator(
        task_id='extract_apod',
        http_conn_id='nasa_api',  ## Connection ID Defined In Airflow For NASA API
        endpoint='planetary/apod', ## NASA API enpoint for APOD
        method='GET',
        data={"api_key":"{{ conn.nasa_api.extra_dejson.api_key}}"}, ## USe the API Key from the connection
        response_filter=lambda response:response.json(), ## Convert response to json
    )

    

    ## Step 3: Transform the data(Pick the information that i need to save)
    @task
    def transform_apod_data(response):
        pass


    ## step 4:  Load the data into Postgres SQL
    @task
    def load_data_to_postgres(apod_data):
        pass



    ## step 5: Verify the data DBViewer


    ## step 6: Define the task dependencies
    ## Extract
    
    ## Transform
    
    ## Load
    