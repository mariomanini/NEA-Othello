class TreeNode:

  def __init__(self,currentBoard,parent=None):
    self.board = currentBoard
    self.__children = []
    self.__parent = parent
    self.__bestchild = None

    #Check if we are in a terminal case. (Both PLayers passing or a winner)

  def getBestMove(self):
    
    return self.__bestchild.board.getmove()

  def evaluate(self):

    if len(self.__children) == 0:
      self.score = self.board.evaluateBoard()
    else:
      for child in self.__children:
        child.evaluate()
      if self.board.isAITurn(): #GetMaximum
        self.score = self.childrenMaxScore()
      else:
        self.score = self.childrenMinScore()

    


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
      boards = self.board.generatePossibleBoards()
      for board in boards:
        child = TreeNode(board,self)
        child.expand(maxLevel) 
        self.__children.append(child)
    if len(self.__children) != 0:
      self.__bestchild = self.__children[0]


