from configparser import ConfigParser


class Config:
  def __init__(self):
    ini_file = "./mob_unit_test.ini"
    self.config_parser = ConfigParser()
    self.config_parser.read(ini_file)

  def get_db_connection(self):
    db = {
      'username': self.config_parser['database']['username'],
      'password': self.config_parser['database']['password'],
      'database': self.config_parser['database']['name'],
      'port': self.config_parser['database']['port'],
      'host': self.config_parser['database']['host']
    }
    return db