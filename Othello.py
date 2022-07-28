


class Game():

  EMPTY = ""
  p1 = "w"
  p2 = "b"

  def __init__(self):
    self.__Board = self.Board()

  def __repr__(self):
    pass

  def Board(self):
    print([Game.EMPTY for _ in range(8)] for _ in range(8))

  def Play(self):
    pass


