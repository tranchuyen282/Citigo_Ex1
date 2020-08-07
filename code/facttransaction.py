from airflow.hooks.mysql_hook import MySqlHook
from airflow.operators.mysql_operator import MySqlOperator

def getRecordsTransaction():
    mysql_hook = MySqlHook(mysql_conn_id ='mysql1',schema='ex1')
    connection = mysql_hook.get_conn()
    cursor = connection.cursor()
    cursor.execute("Select * from fact_transaction where date_id LIKE '%0119'")
    records = cursor.fetchall()
    return records

def insertToFactTransaction(**kwargs):
    mysql_hook = MySqlHook(mysql_conn_id ='mysql2',schema='ex2')
    records = getRecordsTransaction()
    for row in records:
        sql = 'INSERT INTO fact_transaction (user_id, retailer_id,product_id,date_id, quantity) VALUES  (%s,%s,%s,%s,%s)'
        mysql_hook.run(sql, parameters=(row[1],row[2],row[3],row[4],row[5]))