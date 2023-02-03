from Tree import TreeNode
import random


class AIEngine():

  POSSIBLEMOVE = "!"
  AIPLAYER = "w"
  HUMAN = "b"

  def __init__(self,difficulty):
    self.__difficulty = difficulty

  def getBestMove(self,board):

    if self.__difficulty == "Easy":
      return self.__easyaimove(board)




    decisionTree = TreeNode(board)


    decisionTree.expand(3)
    decisionTree.evaluate()
    
    return decisionTree.getBestMove()


  def __easyaimove(self,board):
    possiblemoves = board.getMoveCoordinates()
    randommove = possiblemoves[random.randint(0,len(possiblemoves)-1)]
    return int(randommove[0])+1,int(randommove[-1])+1

