from Board import *

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

    trd = 1
    trdrows = []
    trdcolumns = []
    trFound = False
    try:
      while trFound == False and row-trd >= 0 and col+trd <= 7:
        trdrows.append(row-trd)
        trdcolumns.append(col+trd)
        if self.__board[row-trd][col+trd] == self.__player:
          trFound = True
          for i in range(len(trdrows)):
            self.__board[trdrows[i]][trdcolumns[i]] = self.__player
          break
        trd += 1
    except:
      pass
    trdcolumns.clear()
    trdcolumns.clear()


    
    tld = 1
    tldrows = []
    tldcolumns = []
    tlFound = False
    try:
      while tlFound == False and row-tld >= 0 and col-tld >= 0:
        tldrows.append(row-tld)
        tldcolumns.append(col-tld)
        if self.__board[row-tld][col-tld] == self.__player:
          tlFound = True
          for i in range(len(tldrows)):
            self.__board[tldrows[i]][tldcolumns[i]] = self.__player
        tld += 1
    except:
      pass
    tldrows.clear()
    tldcolumns.clear()
    
    brd = 1
    brdrows = []
    brdcolumns = []
    brFound = False
    try:
      while brFound == False and row+brd <= 7 and col+tld <= 7:
        brdrows.append(row+brd)
        brdcolumns.append(col+brd)
        if self.__board[row+brd][col+brd] == self.__player:
          brFound = True
          for i in range(len(brdrows)):
            self.__board[brdrows[i]][brdcolumns[i]] = self.__player
        brd += 1
    except:
      pass
    brdcolumns.clear()
    brdrows.clear()

    bld = 1
    bldrows = []
    bldcolumns = []
    blFound = False
    try:
      while blFound == False and row+bld <= 7 and col-bld >= 0:
        bldrows.append(row+bld)
        bldcolumns.append(col-bld)
        if self.__board[row+bld][col-bld] == self.__player:
          blFound = True
          for i in range(len(bldrows)):
            self.__board[bldrows[i]][bldcolumns[i]] = self.__player
        bld += 1
    except:
      pass
    bldcolumns.clear()
    bldrows.clear()

    
    

    
    print("here")
    if self.__player == Game.p1: 
      self.__player = Game.p2
    else:
      self.__player = Game.p1





  def play(self,row,col):
    col -= 1
    row -= 1
    if self.__board[row][col] != Game.EMPTY:
      print("Place on an empty square!")
      raise Exception
    else:
      self.__board[row][col] = self.__player

  def result(self):
    return None



    


      




