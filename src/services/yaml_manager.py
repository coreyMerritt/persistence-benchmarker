from datetime import datetime
from typing import List

import yaml

from services.file_manager import FileManager


class YamlManager:
  @staticmethod
  def run_dump_test(test_list: List) -> float:
    yaml_start_timer = datetime.now()
    with open("./test.yaml", "w", encoding='utf-8') as file:
      yaml.dump(test_list, file)
    yaml_stop_time = datetime.now()
    FileManager.delete("./test.yaml")
    yaml_dump_time = (yaml_stop_time - yaml_start_timer).total_seconds()
    return yaml_dump_time
