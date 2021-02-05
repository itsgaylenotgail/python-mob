import schedule
import time

from extract_table_a import ExtractTableA


def job():
  schedule.every(10).seconds.do(ExtractTableA().main)

if __name__ == '__main__':
  job()
  while True:
    schedule.run_pending()
    time.sleep(1)