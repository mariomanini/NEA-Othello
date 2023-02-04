import time
import copy
from Board import Board
import OthelloConfiguration


class Game():


  EMPTY = "_"
  p1 = "b"
  p2 = "w"
  move = "!"

  def __init__(self,gamemode):
    self.board = Board(Game.p1,Game.p2)
    self.__player = Game.p1
    self.__opposingplayer = Game.p2
    self.__gamemode = gamemode
 #A list of the states of the boards as the game progresses

  def __repr__(self):
    output = "\n  " + " ".join(str(i+1) for i in range(8))
    for row in range(8):
      output = output + "\n" + str(row+1) + " " + " ".join(self.board.getboard()[row][i] for i in range(8))
    output = output + "\n" + (f"{self.__player}'s turn: ")
    return output



  def switchplayer(self):
    if self.__player == Game.p1: 
      self.__player = Game.p2
      self.__opposingplayer = Game.p1
    else:
      self.__player = Game.p1
      self.__opposingplayer = Game.p2






  def reviewstate(self):
    if self.__gamemode == "2 Player":
      if self.board.gettotalmoves() == 0:
        if self.__player == Game.p1:
          print("p1 pass")
        else:
          print("p2 pass")
        self.switchplayer()
        return "p"

    if self.__gamemode.split(" ")[-1] == "AI":
      if self.board.gettotalmoves() == 0:
        return "p"


  def checkwinner(self):


      freespaces = 0
      p1counters = 0
      p2counters = 0
      for a in range(8):
        for b in range(8):
          space = self.board.getboard()[a][b]
          if space == Game.p1:
            p1counters += 1
          if space == Game.p2:
            p2counters += 1
          if space == Game.EMPTY or space == Game.move:
            freespaces += 1

      if self.__gamemode.split(" ")[-1] == "AI":
        self.switchplayer()


      if freespaces == 0 or self.reviewstate() == "p":
        print("hello")
        winningplayer = None
        if p1counters > p2counters:
          winningplayer = Game.p1
        if p2counters > p1counters:
          winningplayer = Game.p2
        if p1counters == p2counters:
          winningplayer = "Draw"
        if OthelloConfiguration.OthelloConfig.CHOICE == "t":
          if winningplayer != "Draw":
            print(f"The winner was {winningplayer}!")

        if OthelloConfiguration.OthelloConfig.CHOICE == "g":
          if winningplayer != "Draw":
            if winningplayer == Game.p2:
              if self.__gamemode.split(" ")[-1] == "AI":
                return True, ("The AI wins!")
              else:
                return True, (f"The winner was White!")
            if winningplayer == Game.p1:
              if self.__gamemode.split(" ")[-1] == "AI":
                return True, ("The human wins!")
              else:
                return True, (f"The winner was Black!")
          else:
            return True, ("It was a draw!")

      return False,-1

  def play(self,row,col):
    col -= 1
    row -= 1
    if self.__gamemode == "2 Player":
      if self.board.getboard()[row][col] == Game.move:
        self.board.getboard()[row][col] = self.__player
      else:
        if self.board.getboard()[row][col] != Game.EMPTY:
          if OthelloConfiguration.OthelloConfig.CHOICE == "t":
            print("Place on an empty square!")
            raise Exception
          else:
            return "EmptySquare"
        if self.board.getboard()[row][col] != Game.move:
          if OthelloConfiguration.OthelloConfig.CHOICE == "t":
            print("Can't make that move!")
            raise Exception
          else:
            return "InvalidMove"
    
    if self.__gamemode.split(" ")[-1] == "AI":
      if self.board.getboard()[row][col] == Game.move:
        self.board.getboard()[row][col] = self.__player
      else:
        if self.board.getboard()[row][col] != Game.EMPTY:
          return "EmptySquare"
        if self.board.getboard()[row][col] != Game.move:
          return "InvalidMove"

  def getplayer(self):
    return self.__player

  def getopposingplayer(self):
    return self.__opposingplayer

  def undomove(self):
    if self.board.undomove(self.__gamemode) != -1:
      if self.__gamemode.split(" ")[-1] != "AI":
        self.switchplayer()
    
    

    




    


      




