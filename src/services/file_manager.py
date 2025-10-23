import os


class FileManager:
  @staticmethod
  def delete(file_path: str) -> None:
    os.remove(file_path)
