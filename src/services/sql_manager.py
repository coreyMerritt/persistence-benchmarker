from typing import List


class SqlManager:
  @staticmethod
  def create_table_from_data(
    test_list: List[dict] | List[str] | List[int] | List[float],
    table_name: str,
    cursor,
    engine: str
  ):
    if not test_list:
      raise ValueError("Input list is empty")
    placeholder = "%s" if engine == "mysql" else "?"
    if isinstance(test_list[0], dict):
      sample = test_list[0]
      cols = ", ".join(f"{k} {SqlManager.infer_sql_type(v)}" for k, v in sample.items())
      cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({cols})")
      ph = ", ".join(placeholder for _ in sample)
      return sample.keys(), ph
    else:
      col_type = SqlManager.infer_sql_type(test_list[0])
      cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (value {col_type})")
      return ["value"], placeholder

  @staticmethod
  def infer_sql_type(value):
    if isinstance(value, int):
      return "INTEGER"
    elif isinstance(value, float):
      return "REAL"
    else:
      return "TEXT"