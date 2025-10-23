import json
from datetime import datetime
from typing import List

from services.file_manager import FileManager


class JsonManager:
  @staticmethod
  def run_dump_test(test_list: List) -> float:
    json_start_timer = datetime.now()
    with open("./test.json", "w", encoding='utf-8') as file:
      json.dump(test_list, file)
    json_stop_time = datetime.now()
    FileManager.delete("./test.json")
    json_dump_time = (json_stop_time - json_start_timer).total_seconds()
    return json_dump_time

  @staticmethod
  def run_load_test(test_list: List) -> float:
    with open("./test.json", "w", encoding='utf-8') as file:
      json.dump(test_list, file)
    with open("./test.json", "r", encoding='utf-8') as file:
      json_start_timer = datetime.now()
      _ = json.load(file)
    json_stop_time = datetime.now()
    json_dump_time = (json_stop_time - json_start_timer).total_seconds()
    return json_dump_time
