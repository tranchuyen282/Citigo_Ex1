from airflow.hooks.mysql_hook import MySqlHook
from airflow.operators.mysql_operator import MySqlOperator

def getRecordsRetailer():
    mysql_hook = MySqlHook(mysql_conn_id ='mysql1',schema='ex1')
    connection = mysql_hook.get_conn()
    cursor = connection.cursor()
    cursor.execute("Select * from dim_retailer")
    records = cursor.fetchall()
    return records

def insertToDimRetailer(**kwargs):
    mysql_hook = MySqlHook(mysql_conn_id ='mysql2',schema='ex2')
    records = getRecordsRetailer()
    for row in records:
        sql = 'INSERT INTO dim_retailer (id,name) VALUES  (%s, %s)'
        mysql_hook.run(sql, parameters=(row[0],row[1]))