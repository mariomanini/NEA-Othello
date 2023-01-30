class TreeNode:

  def __init__(self,currentBoard,parent=None):
    self.__currentBoard = currentBoard
    self.__children = []
    self.__parent = parent
    self.__bestchild = None

    #Check if we are in a terminal case. (Both PLayers passing or a winner)

  def getBestMove(self):
    return self.__bestchild.board.getmove()

  def evaluate(self):

    if len(self.__chilren) == 0:
      self.score = self.__currentBoard.evaluate()
    else:
      for child in self.__children:
        child.evaluate()
      if self.__currentBoard.isAITurn(): #GetMaximum
        self.score = self.childrenMaxScore()
      else:
        self.score = self.chidrenMinScore()

    


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



  #Moves

  #Corners Sides

  #Inner Ring




  def getCurrentLevel(self):
    if self.__parent == None:
      return 0
    else:
      return self.__parent.getCurrentLevel() + 1
  


  def expand(self,maxLevel):
    if self.getCurrentLevel() < maxLevel: 
      boards = self.__currentBoard.generatePossibleBoards()
      for board in boards:
        child = TreeNode(board,self)
        child.expand(maxLevel) 
        self.__children.append(child)


