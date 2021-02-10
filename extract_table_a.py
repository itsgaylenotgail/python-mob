from lalb_dao import LALBDAO


class ExtractTableA:
  def __init__(self):
    self.lalbdao = LALBDAO()

  def main(self):
    cntrs = self.lalbdao.get_all_cntrs()
    [print(cntr) for cntr in cntrs]

    data = ("2115840602","CSLU600902","PCC1-OSN-100N", "OOCL SOUTHAMPTON", "LGB10",
            "Long Beach Container Terminal (Pier E)", "America/Los_Angeles","533SCJG", "1")
    new_cntr = self.lalbdao.insert_new_cntr(data)

    print("NEW CONTAINER ADDED WITH ID: " + str(new_cntr))


if __name__ == '__main__':
    ExtractTableA().main()