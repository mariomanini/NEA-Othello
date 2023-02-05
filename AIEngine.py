from Tree import TreeNode
import random


class AIEngine():

  #This is where the program decides how to calculate its move based on the AI's diffculty.

  POSSIBLEMOVE = "!"
  AIPLAYER = "w"
  HUMAN = "b"

  def __init__(self,difficulty):
    self.__difficulty = difficulty

  #// GROUP A SKILL - COMPLEX USER DEFINED ALGORITHMS//

  def getBestMove(self,board):

    if self.__difficulty == "hint":
      return self.__hint(board)

    if self.__difficulty == "Easy":
      return self.__easyaimove(board)

    #For medium difficulty, there is a small chance that the move will be randomised rather than calculated

    if self.__difficulty == "Medium":
      choice = random.randint(1,10)
      if choice <= 2:
        return self.__easyaimove(board)
      else:
        decisionTree = TreeNode(board) #The creation of the Tree where the current state of the board is the root and the possible outcomes of the game are the nodes.
        decisionTree.expand(3) #The parameter that goes here is the depth that the Minimax Algorithm will search until.

    #For hard diffculty, every move will be calculated with a depth of 5.

    if self.__difficulty == "Hard":
      decisionTree = TreeNode(board)
      decisionTree.expand(4)

    decisionTree.evaluate()   

    return decisionTree.getBestMove()


  #The easy AI choses a random move to play. 

  def __easyaimove(self,board):
    possibleMoves = board.getMoveCoordinates()

    #//GROUP A SKILL - LIST OPERATIONS//

    randommove = possibleMoves[random.randint(0,len(possibleMoves)-1)]
    return int(randommove[0])+1,int(randommove[-1])+1

  def __hint(self,board):
    decisionTree = TreeNode(board)
    decisionTree.expand(4)
    decisionTree.evaluate("hint")
    return decisionTree.getBestMove()

