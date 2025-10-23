from datetime import datetime
from typing import List
import pymysql
from services.sql_manager import SqlManager


class MysqlManager:
  @staticmethod
  def run_insert_test(test_list: List) -> float:
    mysql_conn = pymysql.connect(
      host="localhost",
      port=3306,
      user="testuser",
      password="testpass",
      database="testdb",
      autocommit=False
    )
    cur = mysql_conn.cursor()
    columns, placeholders = SqlManager.create_table_from_data(test_list, "test_mysql", cur, engine="mysql")
    if isinstance(test_list[0], dict):
      rows = [tuple(obj[k] for k in columns) for obj in test_list]
      mysql_start_time = datetime.now()
      cur.executemany(
        f"INSERT INTO test_mysql ({', '.join(columns)}) VALUES ({placeholders})",
        rows
      )
    else:
      mysql_start_time = datetime.now()
      cur.executemany(
        "INSERT INTO test_mysql (value) VALUES (%s)",
        [(val,) for val in test_list]
      )
    mysql_conn.commit()
    mysql_stop_time = datetime.now()
    cur.execute("DROP TABLE test_mysql;")
    mysql_conn.commit()
    mysql_conn.close()
    mysql_commit_time = (mysql_stop_time - mysql_start_time).total_seconds()
    return mysql_commit_time
