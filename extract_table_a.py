from lalb_dao import LALBDAO


class ExtractTableA:
  def __init__(self):
    self.lalbdao = LALBDAO()

  def main(self):
    cntrs = self.lalbdao.get_all_cntrs()
    [print(cntr) for cntr in cntrs]


if __name__ == '__main__':
    ExtractTableA().main()