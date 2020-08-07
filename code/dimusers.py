from airflow.hooks.mysql_hook import MySqlHook
from airflow.operators.mysql_operator import MySqlOperator

def getRecordsUser():
    mysql_hook = MySqlHook(mysql_conn_id ='mysql1',schema='ex1')
    connection = mysql_hook.get_conn()
    cursor = connection.cursor()
    cursor.execute("Select * from dim_users")
    records = cursor.fetchall()
    return records

def insertToDimUser(**kwargs):
    mysql_hook = MySqlHook(mysql_conn_id ='mysql2',schema='ex2')
    records = getRecordsUser()
    for row in records:
        sql = 'INSERT INTO dim_users (id,name, email) VALUES  (%s, %s, %s)'
        mysql_hook.run(sql, parameters=(row[0],row[1], row[2]))