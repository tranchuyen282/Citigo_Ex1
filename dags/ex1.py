from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import sys

sys.path.append('/usr/local/airflow/code/')
from dimday import insertToDimDay
from dimweek import insertToDimWeek
from dimmonth import insertToDimMonth
from dimquater import insertToDimQuater
from dimyear import insertToDimYear
from dimusers import insertToDimUser
from dimproduct import insertToDimProduct
from dimretailer import insertToDimRetailer
from dimdate import insertToDimDate
from facttransaction import insertToFactTransaction

default_args = {
    'owner': 'chuyentd',
    'depends_on_past': False,
    'start_date': datetime(2020, 8, 7),
    'email': ['chuyentran282@mail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'ex11',
    default_args=default_args,
    description = "chuyentd_ex1",
    schedule_interval='@once'
)
    
start = BashOperator(
    task_id = 'start',
    bash_command="date",
    dag = dag,
)
done = BashOperator(
    task_id = 'Done',
    bash_command="date",
    dag = dag,
)

insertDataTableDay = PythonOperator(
    task_id = 'insert_day',
    dag = dag,
    python_callable = insertToDimDay,
)
insertDataTableWeek = PythonOperator(
    task_id = 'insert_week',
    dag = dag,
    python_callable = insertToDimWeek,
)
insertDataTableMonth = PythonOperator(
    task_id = 'insert_month',
    dag = dag,
    python_callable = insertToDimMonth,
)
insertDataTableQuater = PythonOperator(
    task_id = 'insert_quater',
    dag = dag,
    python_callable = insertToDimQuater,
)
insertDataTableYear = PythonOperator(
    task_id = 'insert_year',
    dag = dag,
    python_callable = insertToDimYear,
)
insertDataTableUser = PythonOperator(
    task_id = 'insert_user',
    dag = dag,
    python_callable = insertToDimUser,
)
insertDataTableProduct = PythonOperator(
    task_id = 'insert_product',
    dag = dag,
    python_callable = insertToDimProduct,
)
insertDataTableRetailer = PythonOperator(
    task_id = 'insert_retailer',
    dag = dag,
    python_callable = insertToDimRetailer,
)
insertDataTableDate = PythonOperator(
    task_id = 'insert_date',
    dag = dag,
    python_callable = insertToDimDate,
)
insertDataTableTransaction = PythonOperator(
    task_id = 'insert_transaction',
    dag = dag,
    python_callable = insertToFactTransaction,
)
start >> insertDataTableDay >> insertDataTableWeek >> insertDataTableMonth >> insertDataTableQuater >> insertDataTableYear >> insertDataTableDate >> insertDataTableUser >> insertDataTableRetailer >> insertDataTableProduct >> insertDataTableTransaction >> done
# start >> insertDataTableDay







