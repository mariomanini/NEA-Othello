from Board import *

class Game():

  EMPTY = "_"
  p1 = "b"
  p2 = "w"
  move = "!"

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


  def flip(self,row,col,board):
    row -= 1
    col -= 1
    #Normally would be 7,5
    #Indexing means it would be 6,4

    for a in range(8):
      for b in range(8):
        if self.__board[a][b] == Game.move:
          self.__board[a][b] = Game.EMPTY
    
    for i in range(row-1,0,-1):
      if board[i][col] == self.__player:
        for b in range(i+1,row):
          if board[b][col] == self.__player:
            break
          if board[b][col] != Game.EMPTY:
            board[b][col] = self.__player #Checking upwards
          else:
            break
          
    for i in range(row+1,8):
      if board[i][col] == self.__player:
        for b in range(row+1,i):
          if board[b][col] == self.__player:
            break
          if board[b][col] != Game.EMPTY:
            board[b][col] = self.__player #Checking downwards  
          else:
            break

    for i in range(col,0,-1):
      if board[row][i] == self.__player:
        for b in range(i+1,col):
          if board[row][b] == self.__player:
            break
          if board[row][b] != Game.EMPTY:
            board[row][b] = self.__player #Checking left
          else:
            break

    for i in range(col,8):
      if board[row][i] == self.__player:
        for b in range(col+1,i):
          if board[row][b] == self.__player:
            break
          if board[row][b] != Game.EMPTY:
            board[row][b] = self.__player #Checking right
          else:
            break

    trd = 1
    trdrows = []
    trdcolumns = []
    trFound = False
    try:
      while trFound == False and row-trd >= 0 and col+trd <= 7 and board[row-trd][col+trd] != Game.EMPTY:
        trdrows.append(row-trd)
        trdcolumns.append(col+trd)
        if board[row-trd][col+trd] == self.__player:
          trFound = True
          for i in range(len(trdrows)):
            board[trdrows[i]][trdcolumns[i]] = self.__player
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
      while tlFound == False and row-tld >= 0 and col-tld >= 0 and board[row-tld][col-tld] != Game.EMPTY:
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
      while brFound == False and row+brd <= 7 and col+tld <= 7 and board[row+brd][col+brd] != Game.EMPTY:
        brdrows.append(row+brd)
        brdcolumns.append(col+brd)
        if board[row+brd][col+brd] == self.__player:
          brFound = True
          for i in range(len(brdrows)):
            board[brdrows[i]][brdcolumns[i]] = self.__player
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
      while blFound == False and row+bld <= 7 and col-bld >= 0 and board[row+bld][col-bld] != Game.EMPTY:
        bldrows.append(row+bld)
        bldcolumns.append(col-bld)
        if board[row+bld][col-bld] == self.__player:
          blFound = True
          for i in range(len(bldrows)):
            board[bldrows[i]][bldcolumns[i]] = self.__player
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



  def countercount(self):
    totalcounters = 0
    p1counters = 0
    p2counters = 0
    for a in range(8):
      for b in range(8):
        space = self.__board[a][b]
        if space == "w" or space == "b":
          if space == Game.p1:
            totalcounters += 1
            p1counters += 1
          if space == Game.p2:
            totalcounters += 1
            p2counters += 1
    print(f"Total number of counters: {totalcounters} \n {Game.p1}'s counters: {p1counters} \n {Game.p2}'s counters: {p2counters}")
        
  def getboard(self):
    return self.__board
    


  def getpossiblemoves(self):
    p1coords = []
    p2coords = []
    for a in range(8):
      for b in range(8):
        if self.__board[a][b] == Game.p1:
          p1coords.append((a,b))
        if self.__board[a][b] == Game.p2:
          p2coords.append((a,b))
    
    directions = [[1,0],[0,1],[1,1],[0,-1],[-1,0],[-1,1],[-1,-1],[-1,1]]
    if self.__player == Game.p1:
      for place in p1coords:
        for d in directions:
          while True:
            newx = place[0] + d[0] 
            newy = place[1] + d[1]
            if -1 < newx < 8 and -1 < newy < 8:
                if self.__board[newx][newy] != Game.p2:
                  break
                if self.__board[newx + d[0]][newy + d[1]] == Game.EMPTY:
                  self.__board[newx + d[0]][newy + d[1]] = Game.move
            break
    
    if self.__player == Game.p2:
      for place in p2coords:
        for d in directions:
          while True:
            newx = place[0] + d[0] 
            newy = place[1] + d[1]
            if -1 < newx < 8 and -1 < newy < 8:
                if self.__board[newx][newy] != Game.p1:
                  break
                if self.__board[newx + d[0]][newy + d[1]] == Game.EMPTY:
                  self.__board[newx + d[0]][newy + d[1]] = Game.move
            break

      
             
        

    #iterate through all of one colour
    #for each tile of that colour, look in all directions, if there is a trail  of the opposite colour leading to an empty space
    #add the empty space to a list
    
        

  def play(self,row,col):
    col -= 1
    row -= 1
    if self.__board[row][col] == Game.move:
      self.__board[row][col] = self.__player
    else:
      if self.__board[row][col] != Game.EMPTY:
        print("Place on an empty square!")
        raise Exception
      if self.__board[row][col] != Game.move:
        print("Can't make that move!")
        raise Exception

  def result(self):
    return None



    


      




