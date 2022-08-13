
class Game():

  EMPTY = " "
  p1 = "w"
  p2 = "b"

  def __init__(self):
    self.__board = [[Game.EMPTY for _ in range(8)] for _ in range(8)]
    self.__board[4][4] = Game.p1
    self.__board[3][3] = Game.p1
    self.__board[3][4] = Game.p2
    self.__board[4][3] = Game.p2

  def __repr__(self):
    output = "  " + " ".join(str(i+1) for i in range(8))
    for row in range(8):
      output = output + "\n" + str(row+1) + " " + " ".join(self.__board[row][i] for i in range(8))
    return output

  def Play(self):
      pass

if __name__ == "__main__":
    g = Game()
    print(g)



