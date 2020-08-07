from airflow.hooks.mysql_hook import MySqlHook
from airflow.operators.mysql_operator import MySqlOperator

def getRecordsDate():
    mysql_hook = MySqlHook(mysql_conn_id ='mysql1',schema='ex1')
    connection = mysql_hook.get_conn()
    cursor = connection.cursor()
    cursor.execute("Select * from dim_date")
    records = cursor.fetchall()
    return records

def insertToDimDate(**kwargs):
    mysql_hook = MySqlHook(mysql_conn_id ='mysql2',schema='ex2')
    records = getRecordsDate()
    for row in records:
        sql = 'INSERT INTO dim_date (id,day,week,month,quater,year) VALUES  (%s,%s,%s,%s,%s,%s)'
        mysql_hook.run(sql, parameters=(row[0],row[1], row[2],row[3],row[4],row[5]))