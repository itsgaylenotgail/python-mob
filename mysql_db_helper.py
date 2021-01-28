import mysql.connector

from config import Config


class MySqlDbHelper:
  def __init__(self):
    config = Config()
    self.mydb = mysql.connector.connect(
        **config.get_db_connection()
    )
    self.cursor = self.mydb.cursor()

  def get_db_connection(self):
    return self.mydb

  def get_db_cursor(self):
    return self.cursor

