import time
from copy import deepcopy


class Game():


  EMPTY = "_"
  p1 = "b"
  p2 = "w"
  move = "!"

  def __init__(self,gamemode,ui):
    self.__board = [[Game.EMPTY for i in range(8)] for i in range(8)]
    self.__board[4][4] = Game.p2
    self.__board[3][3] = Game.p2
    self.__board[3][4] = Game.p1
    self.__board[4][3] = Game.p1
    self.__player = Game.p1
    self.__winner = False
    self.__gamemode = gamemode
    self.__ui = ui
    self.__boards = [] #A list of the states of the boards as the game progresses

  def __repr__(self):
    output = "\n  " + " ".join(str(i+1) for i in range(8))
    for row in range(8):
      output = output + "\n" + str(row+1) + " " + " ".join(self.__board[row][i] for i in range(8))
    output = output + "\n" + (f"{self.__player}'s turn: ")
    return output

  def flipcounters(self,row,col,board):
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
    
    if self.__ui == "t":
      print(f"Total number of counters: {totalcounters} \n {Game.p1}'s counters: {p1counters} \n {Game.p2}'s counters: {p2counters}")
    if self.__ui == "g":
      return p1counters,p2counters



        
  def getboard(self):
    return self.__board


  def getpossiblemoves(self):
  
    if self.__player == Game.p1:
      opponent = Game.p2
    else:
      opponent = Game.p1
    
    totalmoves = 0
    playercoords = []


    for a in range(8):
      for b in range(8):
        if self.__board[a][b] == self.__player:
          playercoords.append((a,b))

    directions = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
    for place in playercoords: 
      for d in directions: 
        k = 1
        while True:
          newx = place[0] + k *d[0] 
          newy = place[1] + k *d[1] 
          if 0 < newx < 9 and 0 < newy < 9:
            try:
              if self.__board[newx][newy] != opponent:
                break
              if self.__board[newx + d[0]][newy + d[1]] == Game.EMPTY:
                self.__board[newx + d[0]][newy + d[1]] = Game.move
                totalmoves += 1
            except:
                break
          k += 1
          if k > 8:
            break
    


    self.__boards.append(self.__board.copy.deepcopy())
    print(self.__boards)


  def __gettotalmoves(self):
    totalmoves = 0
    for a in range(8):
      for b in range(8):
        if self.__board[a][b] == Game.move:
          totalmoves += 1
    return totalmoves
    
  def reviewstate(self):
    if self.__gamemode == "2 Player":
      if self.__gettotalmoves() == 0:
        if self.__player == Game.p1:
          self.__player = Game.p2
          print(f"{Game.p1} passed because they can't move!")
          return "p"
        elif self.__player == Game.p2:
          self.__player = Game.p1
          print(f"{Game.p2} passed because they can't move!")
          return "p"

    if self.__gamemode.split(" ")[-1] == "AI":
      if self.__gettotalmoves() == 0:
        if self.__player == Game.p1:
          print(f"The Player passed because they couldn't move!")
          return "p"
        elif self.__player == Game.p2:
          print(f"The AI passed because they couldn't move!")
          return "p"

  def checkwinner(self):
      freespaces = 0
      p1counters = 0
      p2counters = 0
      for a in range(8):
        for b in range(8):
          space = self.__board[a][b]
          if space == Game.p1:
            p1counters += 1
          if space == Game.p2:
            p2counters += 1
          if space == Game.EMPTY or space == Game.move:
            freespaces += 1

      if self.__gamemode.split(" ")[-1] == "AI":
        if self.__player == Game.p1:
          self.__player = Game.p2
        else:
          self.__player = Game.p1



      if self.reviewstate() == "p":
        self.__winner = True
        if p1counters > p2counters:
          print(f"The winner was {Game.p1}")
        if p2counters > p1counters:
          print(f"The winner was {Game.p2}")
        if p1counters == p2counters:
            print("It was a draw")
        return True
      if freespaces == 0:
        self.__winner = True
        if p1counters > p2counters:
          print(f"The winner was {Game.p1}")
        if p2counters > p1counters:
          print(f"The winner was {Game.p2}")
        if p1counters == p2counters:
          print("It was a draw")
      return True

  def play(self,row,col):
    col -= 1
    row -= 1
    if self.__gamemode == "2 Player":
      if self.__board[row][col] == Game.move:
        self.__board[row][col] = self.__player
      else:
        if self.__board[row][col] != Game.EMPTY:
          print("Place on an empty square!")
          raise Exception
        if self.__board[row][col] != Game.move:
          print("Can't make that move!")
          raise Exception
    
    if self.__gamemode.split(" ")[-1] == "AI":
      if self.__board[row][col] == Game.move:
        self.__board[row][col] = self.__player
      else:
        if self.__board[row][col] != Game.EMPTY:
          print("Place on an empty square!")
          return -1
        if self.__board[row][col] != Game.move:
          print("Can't make that move!")
          return -1

  def undomove(self):
    self.__movestack.pop()


    




    


      




