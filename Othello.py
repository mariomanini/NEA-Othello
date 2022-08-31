class Game():

  EMPTY = "_"
  p1 = "b"
  p2 = "w"

  def __init__(self):
    self.__board = [[Game.EMPTY for i in range(8)] for i in range(8)]
    self.__board[4][4] = Game.p2
    self.__board[3][3] = Game.p2
    self.__board[3][4] = Game.p1
    self.__board[4][3] = Game.p1
    self.__player = Game.p1

  def __repr__(self):
    output = "\n  " + " ".join(str(i+1) for i in range(8))
    for row in range(8):
      output = output + "\n" + str(row+1) + " " + " ".join(self.__board[row][i] for i in range(8))
    output = output + "\n" + (f"{self.__player} to play: ")
    return output

  
  def flip(self,row,col):
    row -= 1
    col -= 1
    #Normally would be 7,5
    #Indexing means it would be 6,4
    for i in range(row-1,0,-1):
      if self.__board[i][col] == self.__player:
        for b in range(i+1,row):
          if self.__board[b][col] == self.__player:
            break
          if self.__board[b][col] != Game.EMPTY:
            self.__board[b][col] = self.__player #Checking upwards
          else:
            break
          
    for i in range(row+1,8):
      if self.__board[i][col] == self.__player:
        for b in range(row+1,i):
          if self.__board[b][col] == self.__player:
            break
          if self.__board[b][col] != Game.EMPTY:
            self.__board[b][col] = self.__player #Checking downwards  
          else:
            break

    for i in range(col,0,-1):
      if self.__board[row][i] == self.__player:
        for b in range(i+1,col):
          if self.__board[row][b] == self.__player:
            break
          if self.__board[row][b] != Game.EMPTY:
            self.__board[row][b] = self.__player #Checking left
          else:
            break

    for i in range(col,8):
      if self.__board[row][i] == self.__player:
        for b in range(col+1,i):
          if self.__board[row][b] == self.__player:
            break
          if self.__board[row][b] != Game.EMPTY:
            self.__board[row][b] = self.__player #Checking right
          else:
            break

    





    if self.__player == Game.p1: 
      self.__player = Game.p2
    else:
      self.__player = Game.p1
    
    
  

  def play(self,row,col):
    col -= 1
    row -= 1
    if self.__board[row][col] != Game.EMPTY: #If the square is free, place a counter
      pass
    self.__board[row][col] = self.__player #Placing the counter


  def result(self):
    return None



    


      




