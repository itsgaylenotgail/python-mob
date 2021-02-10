from mysql_db_helper import MySqlDbHelper

class LALBDAO:
  def __init__(self):
    self.mysql = MySqlDbHelper()

  def get_all_cntrs(self):
    self.mysql.get_db_cursor().execute(LALBDAO.get_all_cnts_details_sql())
    cntrs = self.mysql.get_db_cursor().fetchall()
    return cntrs

  def insert_new_cntr(self, fields):
    self.mysql.get_db_cursor().execute(LALBDAO.insert_all_cnts_details_sql(), fields)
    cntr = self.mysql.get_db_cursor().lastrowid
    self.mysql.get_db_connection().commit()
    return cntr

  @staticmethod
  def get_all_cnts_details_sql():
    return "SELECT * FROM CNTR_DETAILS"

  @staticmethod
  def insert_all_cnts_details_sql():
    return "INSERT INTO CNTR_DETAILS (BL_NUM, CNTR_NUM, SVVD, VESSEL_NAME, FACILITY_CDE, PICKUP_LOC, " \
           "PICKUP_LOC_TZ, MVMT_SPEC, CHECK_DIGIT ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"