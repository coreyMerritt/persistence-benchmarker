#!/usr/bin/env python3
import yaml

from services.arg_manager import ArgManager
from services.json_manager import JsonManager
from services.mysql_manager import MysqlManager
from services.sqlite_manager import SqliteManager
from services.yaml_manager import YamlManager

ARGS = ArgManager.get_args()
OBJECT_COUNT = ARGS.object_count
TEST_OBJECT = yaml.safe_load("./config/test_object.yml")
TEST_LIST = []
for i in range(OBJECT_COUNT):
  TEST_LIST.append(TEST_OBJECT)


def main():
  json_dump_time = JsonManager.run_dump_test(TEST_LIST)
  sqlite_commit_time = SqliteManager.run_insert_test(TEST_LIST)
  mysql_commit_time = MysqlManager.run_insert_test(TEST_LIST)
  yaml_dump_time = YamlManager.run_dump_test(TEST_LIST)
  lowest_time = min(
    json_dump_time,
    sqlite_commit_time,
    mysql_commit_time,
    yaml_dump_time
  )
  json_load_time = JsonManager.run_load_test(TEST_LIST)
  sqlite_select_all_time = SqliteManager.run_select_all_test(TEST_LIST)
  print(f"    JSON Dump Time: {json_dump_time:>10,.3f}s   {json_dump_time / lowest_time:>10,.2f}x")
  print(f"SQLite Commit Time: {sqlite_commit_time:>10,.3f}s   {sqlite_commit_time / lowest_time:>10,.2f}x")
  print(f" MySQL Commit Time: {mysql_commit_time:>10,.3f}s   {mysql_commit_time / lowest_time:>10,.2f}x")
  print(f"    YAML Dump Time: {yaml_dump_time:>10,.3f}s   {yaml_dump_time / lowest_time:>10,.2f}x")


main()
