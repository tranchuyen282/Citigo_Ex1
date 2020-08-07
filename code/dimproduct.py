from airflow.hooks.mysql_hook import MySqlHook
from airflow.operators.mysql_operator import MySqlOperator

def getRecordsProduct():
    mysql_hook = MySqlHook(mysql_conn_id ='mysql1',schema='ex1')
    connection = mysql_hook.get_conn()
    cursor = connection.cursor()
    cursor.execute("Select * from dim_product")
    records = cursor.fetchall()
    return records

def insertToDimProduct(**kwargs):
    mysql_hook = MySqlHook(mysql_conn_id ='mysql2',schema='ex2')
    records = getRecordsProduct()
    for row in records:
        sql = 'INSERT INTO dim_product (id,product_name) VALUES  (%s, %s)'
        mysql_hook.run(sql, parameters=(row[0],row[1]))