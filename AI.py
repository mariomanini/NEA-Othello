import random

class ai:

  POSSIBLEMOVE = "!"
  EMPTY = "_"

  def __init__(self):
    pass

  

  def __easyaimove(self,boardstate):
    possiblemoves = []
    for a in range(8):
      for b in range(8):
        if boardstate[a][b] == ai.POSSIBLEMOVE:
          possiblemoves.append(f"{a},{b}")
    randommove = possiblemoves[random.randint(0,len(possiblemoves)-1)]
    return int(randommove[0])+1,int(randommove[-1])+1



#form of valuing the importance of each factor, assign values

#Mobility - Number of moves availble to player

#Stablility - Likelihood of each counter being flipped

#Corners / Inner ring 

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

    

  def __mediumaimove(self,boardstate):

    if self.__checkterminalcase(boardstate) == True:
      pass


    #Check if we are in a terminal case. (Both PLayers passing or a winner)


    pass


    #Minimax






  def getmove(self,boardstate,difficulty):
    if difficulty == "Easy":
      return self.__easyaimove(boardstate)
