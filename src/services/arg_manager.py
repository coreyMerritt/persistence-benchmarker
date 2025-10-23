import argparse


class ArgManager:

  @staticmethod
  def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Tests performance for various data storage methods")
    parser.add_argument(
      "object_count",
      type=int,
      help="How many of the item should we test?"
    )
    args = parser.parse_args()
    return args
