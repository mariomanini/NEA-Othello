import random
import copy

class ai:

  POSSIBLEMOVE = "!"
  EMPTY = "_"
  aiplayer = "w"
  human = "b"

  def __init__(self):
    self.__player = ai.aiplayer


  def __getpossiblemoves(self,boardstate):
    possiblemoves = []
    for a in range(8):
      for b in range(8):
        if boardstate[a][b] == ai.POSSIBLEMOVE:
          possiblemoves.append(f"{a},{b}")
    return possiblemoves

  def __easyaimove(self,boardstate):
    possiblemoves = self.__getpossiblemoves(boardstate)
    randommove = possiblemoves[random.randint(0,len(possiblemoves)-1)]
    return int(randommove[0])+1,int(randommove[-1])+1

  def __checkterminalcase(self,boardstate):
    #Board is passed in and if there are no free spaces or both players have passed then it is a terminal case
    fullboard = True
    for a in range(8):
      for b in range(8):
        if boardstate[a][b] == ai.EMPTY or boardstate == ai.POSSIBLEMOVE:
          fullboard = False
    if fullboard == False:
        #Check if both players have passed in the last two cases
      pass
    elif fullboard == True:
      return True




  def getmove(self,boardstate,difficulty):
    if difficulty == "Easy":
      #self.__mediumaimove(boardstate)
      return self.__easyaimove(boardstate)
    #if difficulty == "Medium":


  def trymove(self,boardstate,move): 
    newboard = copy.deepcopy(self.__boardstate)
    move[0] -= 1
    move[-1] -= 1
    row = move[0]
    col = move[-1]
    #flip counters
    for a in range(8):
      for b in range(8):
        if newboard[a][b] == ai.POSSIBLEMOVE:
          newboard[a][b] = ai.EMPTY

    for i in range(row-1,0,-1):
      if newboard[i][col] == self.__player:
        for b in range(i+1,row):
          if newboard[b][col] == self.__player:
            break
          if newboard[b][col] != ai.EMPTY:
            newboard[b][col] = self.__player #Checking upwards
          else:
            break
          
    for i in range(row+1,8):
      if newboard[i][col] == self.__player:
        for b in range(row+1,i):
          if newboard[b][col] == self.__player:
            break
          if newboard[b][col] != ai.EMPTY:
            newboard[b][col] = self.__player #Checking downwards  
          else:
            break

    for i in range(col,0,-1):
      if newboard[row][i] == self.__player:
        for b in range(i+1,col):
          if newboard[row][b] == self.__player:
            break
          if newboard[row][b] != ai.EMPTY:
            newboard[row][b] = self.__player #Checking left
          else:
            break

    for i in range(col,8):
      if newboard[row][i] == self.__player:
        for b in range(col+1,i):
          if newboard[row][b] == self.__player:
            break
          if newboard[row][b] != ai.EMPTY:
            newboard[row][b] = self.__player #Checking right
          else:
            break

    trd = 1
    trdrows = []
    trdcolumns = []
    trFound = False
    try:
      while trFound == False and row-trd >= 0 and col+trd <= 7 and newboard[row-trd][col+trd] != ai.EMPTY:
        trdrows.append(row-trd)
        trdcolumns.append(col+trd)
        if newboard[row-trd][col+trd] == self.__player:
          trFound = True
          for i in range(len(trdrows)):
            newboard[trdrows[i]][trdcolumns[i]] = self.__player
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
      while tlFound == False and row-tld >= 0 and col-tld >= 0 and newboard[row-tld][col-tld] != ai.EMPTY:
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
      while brFound == False and row+brd <= 7 and col+tld <= 7 and newboard[row+brd][col+brd] != ai.EMPTY:
        brdrows.append(row+brd)
        brdcolumns.append(col+brd)
        if newboard[row+brd][col+brd] == self.__player:
          brFound = True
          for i in range(len(brdrows)):
            newboard[brdrows[i]][brdcolumns[i]] = self.__player
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
        if newboard[row+bld][col-bld] == self.__player:
          blFound = True
          for i in range(len(bldrows)):
            newboard[bldrows[i]][bldcolumns[i]] = self.__player
        bld += 1
    except:
      pass
    bldcolumns.clear()
    bldrows.clear()


    #Getting possiblemoves of newboard

    if self.__player == ai.aiplayer:
      opponent = ai.human
    else:
      opponent = ai.aiplayer
    
    totalmoves = 0
    playercoords = []


    for a in range(8):
      for b in range(8):
        if newboard[a][b] == self.__player:
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
              if newboard[newx][newy] != opponent:
                break
              if self.__board[newx + d[0]][newy + d[1]] == ai.EMPTY:
                self.__board[newx + d[0]][newy + d[1]] = ai.POSSIBLEMOVE
                totalmoves += 1
            except:
                break
          k += 1
          if k > 8:
            break

    return newboard


  def switchplayer(self):
    if self.__player == ai.aiplayer:
      self.__player = ai.human
    else:
      self.__player = ai.aiplayer


#form of valuing the importance of each factor, assign values

#Mobility - Number of moves availble to player

#Stablility - Likelihood of each counter being flipped

#Corners / Inner ring 














  def nextpossibleboard(self,boardstate,row,col):
    pass

  #GROUP A - COMPLEX USER DEFINED ALGORITHMS

  def __mediumaimove(self,boardstate):
    
    possiblemoves = self.__getpossiblemoves(boardstate)

    if self.__checkterminalcase(boardstate) == True: #If no moves can be made
      return -1
    possibleboards = []

    for i in range(len(possiblemoves)):
      possibleboards.append(self.__trymove(boardstate,possiblemoves[i]))

    print(possibleboards)



    #Check if we are in a terminal case. (Both PLayers passing or a winner)

