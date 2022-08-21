
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
    self.__player = Game.p1

  def __repr__(self):
    output = "\n  " + " ".join(str(i+1) for i in range(8))
    for row in range(8):
      output = output + "\n" + str(row+1) + " " + " ".join(self.__board[row][i] for i in range(8))
    output = output + "\n" + (f"{self.__player} to play: ")
    return output

  def play(self,row,col):
    col -= 1
    row -= 1
    if self.__board[row][col] != Game.EMPTY: #If the square is free, place a counter
      pass
    self.__board[row][col] = self.__player #Placing the counter
    if self.__player == Game.p1: 
      self.__player = Game.p2
    else:
      self.__player = Game.p1

  def result(self):
    return None
  



    


      




