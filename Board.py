import copy
import OthelloConfiguration
import main
import random


class Board():

  p1 = "b"
  p2 = "w"
  EMPTY = "_"
  move  = "!"

  def __init__(self,player,opposingplayer,otherboard=None,move=None):
    self.__player = player
    self.__opposingplayer = opposingplayer
    if otherboard == None:
      self.__board = [[Board.EMPTY for i in range(8)] for i in range(8)]
      self.__board[4][4] = Board.p2
      self.__board[3][3] = Board.p2
      self.__board[3][4] = Board.p1
      self.__board[4][3] = Board.p1
      initialboard = copy.deepcopy(self.__board)
      self.__boards = [initialboard]
    else:
      self.__board = otherboard
      self.appliedmove = move
      



  def flipcounters(self,row,col,player1):
    row -= 1
    col -= 1
    #Normally would be 7,5
    #Indexing means it would be 6,4
    for a in range(8):
      for b in range(8):
        if self.__board[a][b] == Board.move:
          self.__board[a][b] = Board.EMPTY
    

  
    for i in range(row,-1,-1):
      if self.__board[i][col] == player1:
        for b in range(i+1,row):
          if self.__board[b][col] == player1:
            break
          if self.__board[b][col] != Board.EMPTY:
            self.__board[b][col] = player1 #Checking upwards
          else:
            break
          
    for i in range(row+1,8):
      if self.__board[i][col] == player1:
        for b in range(row+1,i):
          if self.__board[b][col] == player1:
            break
          if self.__board[b][col] != Board.EMPTY:
            self.__board[b][col] = player1 #Checking downwards  
          else:
            break

    for i in range(col,-1,-1):
      if self.__board[row][i] == player1:
        for b in range(i+1,col):
          if self.__board[row][b] == player1:
            break
          if self.__board[row][b] != Board.EMPTY:
            self.__board[row][b] = player1 #Checking left
          else:
            break

    for i in range(col,8):
      if self.__board[row][i] == player1:
        for b in range(col+1,i):
          if self.__board[row][b] == player1:
            break
          if self.__board[row][b] != Board.EMPTY:
            self.__board[row][b] = player1 #Checking right
          else:
            break

    trd = 1
    trdrows = []
    trdcolumns = []
    trFound = False
    try:
      while trFound == False and row-trd >= 0 and col+trd <= 7 and self.__board[row-trd][col+trd] != Board.EMPTY:
        trdrows.append(row-trd)
        trdcolumns.append(col+trd)
        if self.__board[row-trd][col+trd] == player1:
          trFound = True
          for i in range(len(trdrows)):
            self.__board[trdrows[i]][trdcolumns[i]] = player1
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
      while tlFound == False and row-tld >= 0 and col-tld >= 0 and self.__board[row-tld][col-tld] != Board.EMPTY:
        tldrows.append(row-tld)
        tldcolumns.append(col-tld)
        if self.__board[row-tld][col-tld] == player1:
          tlFound = True
          for i in range(len(tldrows)):
            self.__board[tldrows[i]][tldcolumns[i]] = player1
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
      while brFound == False and row+brd <= 7 and col+tld <= 7 and self.__board[row+brd][col+brd] != Board.EMPTY:
        brdrows.append(row+brd)
        brdcolumns.append(col+brd)
        if self.__board[row+brd][col+brd] == player1:
          brFound = True
          for i in range(len(brdrows)):
            self.__board[brdrows[i]][brdcolumns[i]] = player1
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
      while blFound == False and row+bld <= 7 and col-bld >= 0 and self.__board[row+bld][col-bld] != Board.EMPTY:
        bldrows.append(row+bld)
        bldcolumns.append(col-bld)
        if self.__board[row+bld][col-bld] == player1:
          blFound = True
          for i in range(len(bldrows)):
            self.__board[bldrows[i]][bldcolumns[i]] = player1
        bld += 1
    except:
      pass
    bldcolumns.clear()
    bldrows.clear()
    self.__boards.append(copy.deepcopy(self.__board))


  def getpossiblemoves(self,currentplayer,opposingplayer):
    
    totalmoves = 0
    playercoords = []


    for a in range(8):
      for b in range(8):
        if self.__board[a][b] == currentplayer:
          playercoords.append((a,b))

    directions = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
    for place in playercoords: 
      for d in directions: 
        k = 1
        while True:
          newx = place[0] + k *d[0] 
          newy = place[1] + k *d[1] 
          if 0 <= newx < 9 and 0 <= newy < 9:
            try:
              if self.__board[newx][newy] != opposingplayer:
                break
              if self.__board[newx + d[0]][newy + d[1]] == Board.EMPTY and (newx + d[0]) >= 0 and (newy + d[1]) >= 0:
                self.__board[newx + d[0]][newy + d[1]] = Board.move
                totalmoves += 1
            except:
                break
          k += 1
          if k > 8:
            break



  def undomove(self,gamemode):


    if len(self.__boards) == 1:
      return -1
    self.__boards.pop()
    if gamemode.split(" ")[-1] == "AI":
      self.__boards.pop()
    self.__board = copy.deepcopy(self.__boards[-1]) #FIX


  def countercount(self,evaluate=None):

  

    totalcounters = 0
    p1counters = 0
    p2counters = 0
    for a in range(8):
      for b in range(8):
        space = self.__board[a][b]
        if space == "w" or space == "b":
          if space == Board.p1:
            totalcounters += 1
            p1counters += 1
          if space == Board.p2:
            totalcounters += 1
            p2counters += 1
      
    if evaluate == None:
      if OthelloConfiguration.OthelloConfig.CHOICE == "t":
        print(f"Total number of counters: {totalcounters} \n {Board.p1}'s counters: {p1counters} \n {Board.p2}'s counters: {p2counters}")
      if OthelloConfiguration.OthelloConfig.CHOICE == "g":
        return p1counters,p2counters
    if evaluate == "Evaluating":
      return p1counters,p2counters
    else:
      print("not working")
        

  def gettotalmoves(self):
    totalmoves = 0
    for a in range(8):
      for b in range(8):
        if self.__board[a][b] == Board.move:
          totalmoves += 1
    return totalmoves


  def getboard(self):
    return self.__board

  def generatePossibleBoards(self):
    possibleboards = []
    moves = self.getMoveCoordinates()
    for move in moves:
      possibleboards.append(Board(self.__opposingplayer,self.__player,self.trymove(move),move))
    for board in possibleboards:
      board.getpossiblemoves(self.__player,self.__opposingplayer)
    return possibleboards

  def getMoveCoordinates(self):
    movecoords = []
    for a in range(len(self.__board)):
      for b in range(len(self.__board)):
        if self.__board[a][b] == Board.move:
          movecoords.append(f"{a},{b}")
    return movecoords
  
  def trymove(self,move):

    newboard = copy.deepcopy(self.__board)

    row = int(move[0])
    col = int(move[-1])
    for a in range(8):
      for b in range(8):
        if newboard[a][b] == Board.move:
          newboard[a][b] = Board.EMPTY

    

    newboard[row][col] = self.__opposingplayer


    for i in range(row-1,0,-1):
      if newboard[i][col] == self.__opposingplayer:
        for b in range(i+1,row):
          if newboard[b][col] == self.__opposingplayer:
            break
          if newboard[b][col] != Board.EMPTY:
            newboard[b][col] = self.__opposingplayer #Checking upwards
          else:
            break
          
    for i in range(row+1,8):
      if newboard[i][col] == self.__opposingplayer:
        for b in range(row+1,i):
          if newboard[b][col] == self.__opposingplayer:
            break
          if newboard[b][col] != Board.EMPTY:
            newboard[b][col] = self.__opposingplayer #Checking downwards  
          else:
            break

    for i in range(col,0,-1):
      if newboard[row][i] == self.__opposingplayer:
        for b in range(i+1,col):
          if newboard[row][b] == self.__opposingplayer:
            break
          if newboard[row][b] != Board.EMPTY:
            newboard[row][b] = self.__opposingplayer #Checking left
          else:
            break

    for i in range(col,8):
      if newboard[row][i] == self.__opposingplayer:
        for b in range(col+1,i):
          if newboard[row][b] == self.__opposingplayer:
            break
          if newboard[row][b] != Board.EMPTY:
            newboard[row][b] = self.__opposingplayer #Checking right
          else:
            break

    trd = 1
    trdrows = []
    trdcolumns = []
    trFound = False
    try:
      while trFound == False and row-trd >= 0 and col+trd <= 7 and newboard[row-trd][col+trd] != Board.EMPTY:
        trdrows.append(row-trd)
        trdcolumns.append(col+trd)
        if newboard[row-trd][col+trd] == self.__opposingplayer:
          trFound = True
          for i in range(len(trdrows)):
            newboard[trdrows[i]][trdcolumns[i]] = self.__opposingplayer
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
      while tlFound == False and row-tld >= 0 and col-tld >= 0 and newboard[row-tld][col-tld] != Board.EMPTY:
        tldrows.append(row-tld)
        tldcolumns.append(col-tld)
        if self.__board[row-tld][col-tld] == self.__opposingplayer:
          tlFound = True
          for i in range(len(tldrows)):
            self.__board[tldrows[i]][tldcolumns[i]] = self.__opposingplayer
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
      while brFound == False and row+brd <= 7 and col+tld <= 7 and newboard[row+brd][col+brd] != Board.EMPTY:
        brdrows.append(row+brd)
        brdcolumns.append(col+brd)
        if newboard[row+brd][col+brd] == self.__opposingplayer:
          brFound = True
          for i in range(len(brdrows)):
            newboard[brdrows[i]][brdcolumns[i]] = self.__opposingplayer
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
      while blFound == False and row+bld <= 7 and col-bld >= 0 and newboard[row+bld][col-bld] != ai.EMPTY:
        bldrows.append(row+bld)
        bldcolumns.append(col-bld)
        if newboard[row+bld][col-bld] == self.__opposingplayer:
          blFound = True
          for i in range(len(bldrows)):
            newboard[bldrows[i]][bldcolumns[i]] = self.__opposingplayer
        bld += 1
    except:
      pass
    bldcolumns.clear()
    bldrows.clear()

    return newboard

  def isFull(self):
    FullBoard = True
    for a in range(8):
      for b in range(8):
        if self.__board[a][b] == Board.EMPTY or self.__board == Board.move:
          FullBoard = False
    return FullBoard
 
  def isAITurn(self):
    if self.__player == Board.p2:
      return True
  
  def getmove(self):
    self.appliedmove = f"{int(self.appliedmove[0])+1},{int(self.appliedmove[-1])+1}"
    return self.appliedmove

  def evaluateBoard(self):

    totalScore = 0

    if self.isFull == True:
      results = self.countercount("Evaluating")
      if results[0] > results [1]:
        return -100
      else:
        if results[0] == results[1]:
          return 0 
        else:
          return 100

    else:

      #Moves
      moveScore = 0
      moveScore = self.gettotalmoves()
      totalScore += moveScore

      

      #Corners
      cornerScore = 0
      if self.__board[0][0] == Board.move:
        cornerScore += 10
      if self.__board[0][7] == Board.move:
        cornerScore += 10
      if self.__board[7][0] == Board.move:
        cornerScore += 10
      if self.__board[7][7] == Board.move:
        cornerScore += 10



      totalScore += cornerScore

      edgeScore = 0
      for col in range(1,7):
        pass
        
      #Edges



      #Inner

    



      return totalScore
  
      












  

  

  