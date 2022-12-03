
class ai:

  possiblemove = "!"

  def __init__(self):
    pass

  def getmove(boardstate):
    for a in range(8):
      for b in range(8):
        if boardstate[a][b] == ai.possiblemove:
          print(boardstate[a][b])
          #return (a,b)

    