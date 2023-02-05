class TreeNode:

  #//GROUP A SKILL - TREE AND TREE TRAVERSAL//

  def __init__(self,currentBoard,parent=None):
    self.board = currentBoard
    self.__children = []
    self.__parent = parent
    self.__bestchild = None


  def getBestMove(self):
    return self.__bestchild.board.getMove()



  #This function will find which child node has the highest score. 
  # If it's the AI's turn, it looks for the maximising value, if it's the player's turn, it looks for the minimising value

  def evaluate(self,hint=None):

    if hint == None:
      if len(self.__children) == 0:
        self.score = self.board.evaluateBoard()
      else:
        for child in self.__children:
          child.evaluate()
        
        if self.board.isAITurn(): #GetMaximum
          self.score = self.childrenMaxScore()
        else:
          self.score = self.childrenMinScore()

    elif hint == "hint":
       print("here")
       if len(self.__children) == 0:
        self.score = self.board.evaluateBoard("hint")
       else:
        for child in self.__children:
          child.evaluate("hint")

        #When finding a hint for the player, these lines are reversed so that the AI is minimising and the player is maximising.
        
        if self.board.isAITurn(): 
           self.score = self.childrenMinScore()              
        else:
          self.score = self.childrenMaxScore()


  def childrenMaxScore(self):
    score = -100
    for child in self.__children:
      if child.score > score:
        score = child.score
        self.__bestchild = child
    return score

  def childrenMinScore(self):
    score = 100
    for child in self.__children:
      if child.score < score:
        score = child.score
    return score


  #The depth of a node will always be the depth of its parent node + 1

  def getCurrentLevel(self):
    if self.__parent == None:
      return 0
    else:
      return self.__parent.getCurrentLevel() + 1
  


  def expand(self,maxLevel):
    if self.getCurrentLevel() < maxLevel: 
      boards = self.board.generatePossibleBoards()
      for board in boards:

        #Each child node is a possible outcome of the game.

        child = TreeNode(board,self)

        #Recursion - Each node's child will keep expanding until their currentlevel is equal to maxLevel

        #//GROUP A SKILL - RECURSIVE ALGORITHMS//

        child.expand(maxLevel) 
        self.__children.append(child)

    #Initialising the best child. This is to prevent there being no best child.

    if len(self.__children) != 0:
      self.__bestchild = self.__children[0]


    

