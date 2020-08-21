import os
from airflow.models import DAG, Variable
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator
from airflow.contrib.operators.mysql_to_gcs import MySqlToGoogleCloudStorageOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from schema.log_mykiot.schema_dlk import TableLogMyKiot
from schema.log_mykiot.schema_dwh import TableLogMyKiotDWH
from google.cloud import storage
from airflow.contrib.hooks.gcs_hook import GoogleCloudStorageHook
from io import StringIO
from datetime import datetime, timedelta
import logging
import re
import time
import csv

BUSINESS_DATE = Variable.get("business_date")
BQ_PROJECT = Variable.get("bq_project")
STG_DB_NAME = Variable.get("bq_staging_crm")

DWH_DB_NAME = Variable.get("bq_warehouse_crm")
NOW = datetime.now() + timedelta(days=-1)
NOW = NOW.strftime('%Y%m%d')

if BUSINESS_DATE == "None" or BUSINESS_DATE is None:
    now = datetime.now() + timedelta(days=-1)
    BUSINESS_DATE = now.strftime('%Y%m%d')


def test_read_file_from_GCS(ds, **kwargs):
    # 1. read file from GCS -> blob
    logging.warning("1. CONNECT GCS")
    start_time_total = time.time()
    client = storage.Client.from_service_account_json('/usr/local/airflow/data_transform_code/perm.json')
    bucket = client.get_bucket('mykiot_dev')
    #list_blob = client.list_blobs('mykiot_dev', prefix='log_access_chuyentd_test')
    list_blob = bucket.list_blobs(prefix='log_access_chuyentd_test')
    for blob in list_blob:
        if '.log' in blob.name:
            logging.info('Start convert blob: {}'.format(blob.name))
            



    # for blob in list_blob:
    #     logging.info('Start convert file {}'.format(str(blob)))
    #     blob_downloaded = blob.download_as_string()
    #     blob_downloaded = blob_downloaded.decode('utf-8')
    #     end_time = time.time()
    #     logging.warning("END CONNECT AND DOWN BOLB: %f ms" % ((end_time - start_time_total) * 1000))
    #     # 2. convert to csv
    #     logging.warning("START CONVERT TO CSV")
    #     start_time = time.time()
    #
    #     csv_file_name = '/tmp/etl/'
    #     list_string = blob_downloaded.split('\n')
    #     pattern = re.compile(r'(?P<host>\S+).(?P<rfc1413ident>\S+).(?P<user>\S+).\[(?P<datetime>\S+ \+[0-9]{4})]."(?P<httpverb>\S+) (?P<url>\S+) (?P<httpver>\S+)" (?P<status>[0-9]+) (?P<size>\S+) "(?P<referer>.*)" "(?P<useragent>.*)"\s*\Z')
    #     # str_csv = 'host,ident,user,time,verb,url,httpver,status,size,referer,useragent'
    #     # write to file csv in local
    #     index = 0
    #     with open(csv_file_name, 'w', newline='') as out:
    #         csv_out = csv.writer(out)
    #         csv_out.writerow(
    #             ['host', 'ident', 'user', 'time', 'verb', 'url', 'httpver', 'status', 'size', 'referer', 'useragent'])
    #         for line in list_string:
    #             index += 1
    #             if len(line) > 0:
    #                 m = pattern.match(line)
    #                 result = m.groups()
    #                 list_result = list(result)
    #                 list_result[3] = datetime.strptime(list_result[3], '%d/%b/%Y:%H:%M:%S +0700')
    #                 # str_row = ','.join(str(s) for s in list_result)
    #                 # str_csv = str_csv+'\n'+str_row
    #                 result = tuple(list_result)
    #                 csv_out.writerow(result)
    # end_time = time.time()
    # logging.warning("END CONVERT TO CSV {} ms".format((end_time-start_time)*1000))
    #
    # # 3. upload to GCS
    # logging.warning("START UPLOAD TO GCS")
    # start_time = time.time()
    #
    # blob2 = bucket.blob('log_access_chuyentd_test/access.csv')
    # #blob2.upload_from_string(str_csv)
    # blob2.upload_from_filename('/tmp/etl/access.csv')


    end_time = time.time()
    #logging.warning("END UPLOAD TO GCS {} ms".format((end_time - start_time) * 1000))
    logging.warning("TOTAL TIME {} ms".format((end_time - start_time_total) * 1000))


def sub_convert_file_log_mykiot(parent_dag_name, child_dag_name, args):
    dag_subdag = DAG(
        dag_id='%s.%s' % (parent_dag_name, child_dag_name),
        default_args=args,
        schedule_interval=None
    )
    PythonOperator(
        task_id="read_file_from_gcs",
        provide_context=True,
        python_callable=test_read_file_from_GCS,
        dag=dag_subdag
    )
    return dag_subdag


def sub_load_staging_mykiot(parent_dag_name, child_dag_name, args):
    dag_subdag = DAG(
        dag_id='%s.%s' % (parent_dag_name, child_dag_name),
        default_args=args,
        schedule_interval=None
    )
    # Load from csv gcs to STG
    table_extract = TableLogMyKiot()
    for p in table_extract.ALL_TABLES:
         source_uris = ["log/{}-{}-{}/*".format(BUSINESS_DATE[0:4], BUSINESS_DATE[4:6], BUSINESS_DATE[6:8])]
         GoogleCloudStorageToBigQueryOperator(
            task_id="{}_to_stg".format(p.TABLE_NAME),
            execution_timeout=timedelta(minutes=30),
            google_cloud_storage_conn_id='bq_kvp',
            bucket="{{ var.value.gc_bucket_mykiot }}",
            source_objects=source_uris,  # File from bucket
            source_format="CSV",
            field_delimiter=',',
            skip_leading_rows = 1,
            bigquery_conn_id='bq_kvp',
            destination_project_dataset_table='{}.{}'.format('{{ var.value.bq_staging_mykiot }}', p.TABLE_NAME),
            schema_fields=p.COLUMNS,
            create_disposition='CREATE_IF_NEEDED',
            write_disposition='WRITE_TRUNCATE',
            dag=dag_subdag
        )
    return dag_subdag


def sub_load_wh_mykiot(parent_dag_name, child_dag_name, args):
    dag_subdag = DAG(
        dag_id='%s.%s' % (parent_dag_name, child_dag_name),
        default_args=args,
        schedule_interval=None
    )

    table_extract = TableLogMyKiotDWH()

    for p in table_extract.ALL_TABLES:
        load_to_dwh = BigQueryOperator(
            task_id="{}_to_dwh".format(p.TABLE_NAME),
            execution_timeout= timedelta(minutes=30),
            destination_dataset_table="{}.{}".format('{{ var.value.bq_warehouse_mykiot }}', p.TABLE_NAME),
            bigquery_conn_id="bq_kvp",
            write_disposition="WRITE_APPEND",
            create_disposition='CREATE_IF_NEEDED',
            time_partitioning=p.TIME_PARTITIONING,
            sql="sql/dwh/log_mykiot/load_{}.sql".format(p.TABLE_NAME),
            params={"business_date": BUSINESS_DATE, "table_name": p.TABLE_NAME },
            use_legacy_sql=False,
            dag=dag_subdag
        )

        delete_before_load_to_dwh = BigQueryOperator(
            task_id="DELETE_{}".format(p.TABLE_NAME),
            execution_timeout=timedelta(minutes=30),
            bigquery_conn_id="bq_kvp",
            sql="DELETE FROM `{}.{}` WHERE BUSINESS_DATE = '{}'".format('{{ var.value.bq_warehouse_mykiot }}', p.TABLE_NAME,
                                                                        BUSINESS_DATE),
            params={"business_date": BUSINESS_DATE, "table_name": p.TABLE_NAME},
            use_legacy_sql=False,
            dag=dag_subdag
        )

        delete_before_load_to_dwh >> load_to_dwh
    return dag_subdag