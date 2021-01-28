from mysql_db_helper import MySqlDbHelper

class LALBDAO:
  def __init__(self):
    self.mysql = MySqlDbHelper()

  def get_all_cntrs(self):
    self.mysql.get_db_cursor().execute(LALBDAO.get_all_cnts_details_sql())
    cntrs = self.mysql.get_db_cursor().fetchall()
    return cntrs

  @staticmethod
  def get_all_cnts_details_sql():
    return "SELECT * FROM CNTR_DETAILS"