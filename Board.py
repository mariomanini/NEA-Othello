import copy
import OthelloConfiguration
import main
import random


class Board():

  p1 = "b"
  p2 = "w"
  EMPTY = "_"
  move  = "!"

  def __init__(self,player,opposingPlayer,otherboard=None,move=None):
    self.__player = player
    self.__opposingplayer = opposingPlayer
    if otherboard == None:
      #Creation of the board.

      #//GROUP B SKILL - MULTI-DIMENSIONAL ARRAYS// 

      self.__board = [[Board.EMPTY for i in range(8)] for i in range(8)]
      self.__board[4][4] = Board.p2
      self.__board[3][3] = Board.p2
      self.__board[3][4] = Board.p1
      self.__board[4][3] = Board.p1
      initialboard = copy.deepcopy(self.__board)
      #The list which contains each state of the board every time a move is made.
      #//GROUP A SKILL - STACK//
      self.__boards = [initialboard]
    else:
      #This is for when other board objects are created within the decision tree.
      self.__board = otherboard
      self.appliedMove = move
      

  #This function is called to flip the counters which meet the correct conditions.

  def flipCounters(self,row,col,player1):

    row -= 1
    col -= 1

    #Temporarily removing the indicators for where moves can be played so that this function can be run.

    for a in range(8):
      for b in range(8):
        if self.__board[a][b] == Board.move:
          self.__board[a][b] = Board.EMPTY

    #Checking all cells directly upwards of where the move was played.
    
    for i in range(row,-1,-1):
      if self.__board[i][col] == player1:
        for b in range(i+1,row):
          if self.__board[b][col] == player1:
            break
          if self.__board[b][col] != Board.EMPTY:
            self.__board[b][col] = player1 
          else:
            break
          
    #Checking downwards.
    
    for i in range(row+1,8):
      if self.__board[i][col] == player1:
        for b in range(row+1,i):
          if self.__board[b][col] == player1:
            break
          if self.__board[b][col] != Board.EMPTY:
            self.__board[b][col] = player1 #Checking downwards  
          else:
            break

    #Checking left.

    for i in range(col,-1,-1):
      if self.__board[row][i] == player1:
        for b in range(i+1,col):
          if self.__board[row][b] == player1:
            break
          if self.__board[row][b] != Board.EMPTY:
            self.__board[row][b] = player1 
          else:
            break
    
    #Checking right.

    for i in range(col,8):
      if self.__board[row][i] == player1:
        for b in range(col+1,i):
          if self.__board[row][b] == player1:
            break
          if self.__board[row][b] != Board.EMPTY:
            self.__board[row][b] = player1 #Checking right
          else:
            break

    #Checking in the north east direction.

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

    #Checking north west.

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

    #Checking south east
    
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

    #Checking south west

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

    #The board at this point is noted down which is used if the user wants to undo their move.

    self.__boards.append(copy.deepcopy(self.__board))

  #This function will mark each cell where the player is able to place a counter.

  def getPossibleMoves(self,currentPlayer,opposingPlayer):
    
    playerCoords = []

    for a in range(8):
      for b in range(8):
        if self.__board[a][b] == currentPlayer:
          playerCoords.append((a,b))



    directions = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

    #For each cell where there is a counter on the player's colour

    for place in playerCoords: 

      #Check in each direction

      for d in directions: 
        k = 1
        while True:

          #//GROUP C SKILL - MATHEMATICAL CALCULATIONS

          newx = place[0] + k *d[0] 
          newy = place[1] + k *d[1] 
          if 0 <= newx < 9 and 0 <= newy < 9:
            try:

              #If you find a counter which is not of the opposite colour, stop checking in that direction.

              if self.__board[newx][newy] != opposingPlayer:
                break

              #If an empty space is found, mark the cell as one where the player can play.

              if self.__board[newx + d[0]][newy + d[1]] == Board.EMPTY and (newx + d[0]) >= 0 and (newy + d[1]) >= 0:
                self.__board[newx + d[0]][newy + d[1]] = Board.move
            except:
                break
          k += 1
          if k > 8:
            break


  #Takes back the most recent move.

  def undoMove(self,gamemode):


    #//GROUP A SKILL - STACK OPERATIONS//
  
    #You cannot undo when no moves have been made yet.

    if len(self.__boards) == 1: 
      return -1

    #Pop the most recent board state

    self.__boards.pop()

    #If the player is playing against the computer, pop two states since you will have to undo the computer's move as well as your own.

    if gamemode.split(" ")[-1] == "AI":
      self.__boards.pop()

    #The new board is the last item in the list of states after the pop has happened.

    self.__board = copy.deepcopy(self.__boards[-1]) #FIX

  #Returns the number of counters of each colour.

  def counterCount(self,evaluate=None):

    totalCounters = 0
    p1Counters = 0
    p2Counters = 0
    for a in range(8):
      for b in range(8):
        space = self.__board[a][b]
        if space == "w" or space == "b":
          if space == Board.p1:
            totalCounters += 1
            p1Counters += 1
          if space == Board.p2:
            totalCounters += 1
            p2Counters += 1
      
    if evaluate == None:
      if OthelloConfiguration.OthelloConfig.CHOICE == "t":
        print(f"Total number of counters: {totalCounters} \n {Board.p1}'s counters: {p1Counters} \n {Board.p2}'s counters: {p2Counters}")
      if OthelloConfiguration.OthelloConfig.CHOICE == "g":
        return p1Counters,p2Counters

    #This function is also called when the board's value is being measured.
    
    if evaluate == "Evaluating":
      return p1Counters,p2Counters

        
  #Returns the number of moves.

  def getTotalMoves(self):
    totalMoves = 0
    for a in range(8):
      for b in range(8):
        if self.__board[a][b] == Board.move:
          totalMoves += 1
    return totalMoves

  def getBoard(self):
    return self.__board

  #Applies the "tryMove" function to the board for each possible move there is. This is how the next states are generated.

  def generatePossibleBoards(self):
    possibleBoards = []
    moves = self.getMoveCoordinates()
    for move in moves:
      possibleBoards.append(Board(self.__opposingplayer,self.__player,self.tryMove(move),move))
    for board in possibleBoards:
      board.getPossibleMoves(self.__player,self.__opposingplayer)
    return possibleBoards

  def getMoveCoordinates(self):
    moveCoords = []
    for a in range(len(self.__board)):
      for b in range(len(self.__board)):
        if self.__board[a][b] == Board.move:
          moveCoords.append(f"{a},{b}")
    return moveCoords
  
  #This function is similar to the flip counters move. However, it will make the move that it is passed on a copy of the board and simulate the move on the board.

  def tryMove(self,move):

    newBoard = copy.deepcopy(self.__board)

    row = int(move[0])
    col = int(move[-1])
    for a in range(8):
      for b in range(8):
        if newBoard[a][b] == Board.move:
          newBoard[a][b] = Board.EMPTY

    newBoard[row][col] = self.__opposingplayer

    for i in range(row-1,0,-1):
      if newBoard[i][col] == self.__opposingplayer:
        for b in range(i+1,row):
          if newBoard[b][col] == self.__opposingplayer:
            break
          if newBoard[b][col] != Board.EMPTY:
            newBoard[b][col] = self.__opposingplayer 
          else:
            break
          
    for i in range(row+1,8):
      if newBoard[i][col] == self.__opposingplayer:
        for b in range(row+1,i):
          if newBoard[b][col] == self.__opposingplayer:
            break
          if newBoard[b][col] != Board.EMPTY:
            newBoard[b][col] = self.__opposingplayer 
          else:
            break

    for i in range(col,0,-1):
      if newBoard[row][i] == self.__opposingplayer:
        for b in range(i+1,col):
          if newBoard[row][b] == self.__opposingplayer:
            break
          if newBoard[row][b] != Board.EMPTY:
            newBoard[row][b] = self.__opposingplayer
          else:
            break

    for i in range(col,8):
      if newBoard[row][i] == self.__opposingplayer:
        for b in range(col+1,i):
          if newBoard[row][b] == self.__opposingplayer:
            break
          if newBoard[row][b] != Board.EMPTY:
            newBoard[row][b] = self.__opposingplayer 
            break

    trd = 1
    trdrows = []
    trdcolumns = []
    trFound = False
    try:
      while trFound == False and row-trd >= 0 and col+trd <= 7 and newBoard[row-trd][col+trd] != Board.EMPTY:
        trdrows.append(row-trd)
        trdcolumns.append(col+trd)
        if newBoard[row-trd][col+trd] == self.__opposingplayer:
          trFound = True
          for i in range(len(trdrows)):
            newBoard[trdrows[i]][trdcolumns[i]] = self.__opposingplayer
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
      while tlFound == False and row-tld >= 0 and col-tld >= 0 and newBoard[row-tld][col-tld] != Board.EMPTY:
        tldrows.append(row-tld)
        tldcolumns.append(col-tld)
        if newBoard[row-tld][col-tld] == self.__opposingplayer:
          tlFound = True
          for i in range(len(tldrows)):
            newBoard[tldrows[i]][tldcolumns[i]] = self.__opposingplayer
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
      while brFound == False and row+brd <= 7 and col+tld <= 7 and newBoard[row+brd][col+brd] != Board.EMPTY:
        brdrows.append(row+brd)
        brdcolumns.append(col+brd)
        if newBoard[row+brd][col+brd] == self.__opposingplayer:
          brFound = True
          for i in range(len(brdrows)):
            newBoard[brdrows[i]][brdcolumns[i]] = self.__opposingplayer
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
      while blFound == False and row+bld <= 7 and col-bld >= 0 and newBoard[row+bld][col-bld] != ai.EMPTY:
        bldrows.append(row+bld)
        bldcolumns.append(col-bld)
        if newBoard[row+bld][col-bld] == self.__opposingplayer:
          blFound = True
          for i in range(len(bldrows)):
            newBoard[bldrows[i]][bldcolumns[i]] = self.__opposingplayer
        bld += 1
    except:
      pass

    bldcolumns.clear()
    bldrows.clear()

    return newBoard

  #Returns True if the board is full.

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
  
  #Returns the move which resulted in the board state. Used in the Minimax algorithm for tracing which moves led to which states.

  def getMove(self):
    self.appliedMove = f"{int(self.appliedMove[0])+1},{int(self.appliedMove[-1])+1}"
    return self.appliedMove

  #The function which calculates a score based on its state.

  def evaluateBoard(self,hint=None):

    totalScore = 0

    #If the board is full, the score will depend on who the winner is.




    if self.isFull == True:
      results = self.counterCount("Evaluating")

      #If the player wins, this is not in favour for the computer.

      if hint == None:
        if results[0] > results [1]:
          return -1000
        else:
          if results[0] == results[1]:
            return 0 
          else:

            #If the AI wins, return this state as having the most favourable score.

            return 1000
      
      elif hint == "hint":
        if results[1] > results [0]:
          return -1000
        else:
          if results[1] == results[0]:
            return 0 
          else:

            #If the AI wins, return this state as having the most favourable score.

            return 1000

    else:

      #States where there are counters of the player's colour on the corner are favourable because they cannot be flipped once they are placed on the corner.

      stabilityScore = 0
      if self.__board[0][0] == self.__player:
        stabilityScore += 30
      if self.__board[0][7] == self.__player:
        stabilityScore += 30
      if self.__board[7][0] == self.__player:
        stabilityScore += 30
      if self.__board[7][7] == self.__player:
        stabilityScore += 30

      if self.__board[0][0] == self.__opposingplayer:
        stabilityScore -= 30
      if self.__board[0][7] == self.__opposingplayer:
        stabilityScore -= 30
      if self.__board[7][0] == self.__opposingplayer:
        stabilityScore -= 30
      if self.__board[7][7] == self.__opposingplayer:
        stabilityScore -= 30
      #The "Mobility" of the board state is how many possible moves the player has. It is more beneficial to have more moves.

      moveScore = 0
      moveScore = self.getTotalMoves()
    
      #Corners are the most important cells to play on in the game. Therefore, having the opportunity to play on one gives the board a high score.      

      cornerScore = 0
      if self.__board[0][0] == Board.move:
        cornerScore += 50
      if self.__board[0][7] == Board.move:
        cornerScore += 50
      if self.__board[7][0] == Board.move:
        cornerScore += 50
      if self.__board[7][7] == Board.move:
        cornerScore += 50

    

      #Edges are also very important

      edgeScore = 0
      for col in range(1,7):
        if self.__board[0][col] == Board.move or self.__board[7][col] == Board.move:
          edgeScore += 10
      for row in range(1,7):
        if self.__board[row][0] == Board.move or self.__board[row][7] == Board.move:
          edgeScore += 10
        
      #Playing moves on the inner ring is not optimal in Othello, so for every move you have on this inner ring, the score will be decreased.

      innerRingScore = 0
      for col in range(1,7):
        if self.__board[1][col] == Board.move or self.__board[6][col] == Board.move:
          innerRingScore -= 3
      for row in range(2,6):
        if self.__board[row][1] == Board.move or self.__board[row][6] == Board.move:
          innerRingScore -= 3

      totalScore += moveScore + cornerScore + edgeScore + innerRingScore + stabilityScore

      return totalScore
  
      












  

  

  