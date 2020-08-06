import mysql.connector

import json
class DataBase:
    def __init__(self):
        self.con = None
        self.cur = None

        self._connect()

    def _init_from_json(self, path):
        with open(path) as f:
            mysql_config = json.load(f)
        return mysql_config

    def _connect(self):
        connection_config_dict = {
            'user': 'chuyentd',
            'password': 'chuyentd282',
            'host': 'localhost',
            'database': 'ex1',
            'raise_on_warnings': True,
            'use_pure': False,
            'autocommit': True
        }
        if (self.con is not None) or (self.cur is not None):
            return

        self.con = mysql.connector.connect(**connection_config_dict)
        self.cur = self.con.cursor()

    def insert_to(self, table, listObj):
        query = {
            "dim_users" : "INSERT INTO dim_users (name, email) VALUES  (%s, %s)",
            "dim_product": "INSERT INTO dim_product (product_name) VALUES  (%s)",
            "dim_date": "INSERT INTO dim_date (id, day,week,month,quater,year) VALUES  (%s, %s, %s,%s,%s,%s)",
            "dim_day":"INSERT INTO dim_day (id,_day) VALUES  (%s, %s)",
            "dim_month" :"INSERT INTO dim_month (id, _month) VALUES  (%s, %s)",
            "dim_quater":"INSERT INTO dim_quater (id, _quater) VALUES  (%s, %s)",
            "dim_retailer":"INSERT INTO dim_retailer (name) VALUES  (%s)",
            "dim_week":"INSERT INTO dim_week (id, _week) VALUES  (%s, %s)",
            "dim_years":"INSERT INTO dim_years (id, _year) VALUES  (%s, %s)",
            "dim_date": "INSERT INTO dim_date (id,day,week,month,quater,year) VALUES  (%s,%s,%s,%s,%s,%s)",
            "fact_transaction": "INSERT INTO fact_transaction (user_id, retailer_id,product_id,date_id, quantity) VALUES  (%s,%s,%s,%s,%s)"

        }

        self.cur.executemany(query[table], listObj)
        self.con.commit()
        print(self.cur.rowcount, " inserted")

