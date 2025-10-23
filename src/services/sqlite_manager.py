from datetime import datetime
import sqlite3
from typing import List
from services.file_manager import FileManager
from services.sql_manager import SqlManager


class SqliteManager:
  @staticmethod
  def run_insert_test(test_list: List) -> float:
    sqlite_conn = sqlite3.connect("./test.db")
    cur = sqlite_conn.cursor()
    columns, placeholders = SqlManager.create_table_from_data(test_list, "test_sqlite", cur, "sqlite")
    if isinstance(test_list[0], dict):
      rows = [tuple(obj[k] for k in columns) for obj in test_list]
      sqlite_start_time = datetime.now()
      cur.executemany(
        f"INSERT INTO test_sqlite ({', '.join(columns)}) VALUES ({placeholders})",
        rows
      )
    else:
      sqlite_start_time = datetime.now()
      cur.executemany(
        "INSERT INTO test_sqlite (value) VALUES (?)",
        [(val,) for val in test_list]
      )
    sqlite_conn.commit()
    sqlite_stop_time = datetime.now()
    sqlite_conn.close()
    FileManager.delete("./test.db")
    sqlite_commit_time = (sqlite_stop_time  - sqlite_start_time).total_seconds()
    return sqlite_commit_time

  @staticmethod
  def run_select_all_test(test_list: List) -> float:
    sqlite_conn = sqlite3.connect("./test.db")
    cur = sqlite_conn.cursor()
    columns, placeholders = SqlManager.create_table_from_data(test_list, "test_sqlite", cur, "sqlite")
    if isinstance(test_list[0], dict):
      rows = [tuple(obj[k] for k in columns) for obj in test_list]
      cur.executemany(
        f"INSERT INTO test_sqlite ({', '.join(columns)}) VALUES ({placeholders})",
        rows
      )
    else:
      cur.executemany(
        "INSERT INTO test_sqlite (value) VALUES (?)",
        [(val,) for val in test_list]
      )
    sqlite_conn.commit()
    sqlite_start_time = datetime.now()
    cur.execute("SELECT * FROM test_sqlite;")
    rows = cur.fetchall()
    sqlite_stop_time = datetime.now()
    sqlite_conn.close()
    FileManager.delete("./test.db")
    sqlite_select_time = (sqlite_stop_time  - sqlite_start_time).total_seconds()
    return sqlite_select_time
