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
    self.__winner = False
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
          self.__player = Game.p2
          if OthelloConfiguration.OthelloConfig.CHOICE == "t":
            print(f"{Game.p1} passed because they can't move!")
            return "p"
          else:
            return "p",(f"{Game.p1} passed because they can't move!")
        elif self.__player == Game.p2:
          self.__player = Game.p1
          if OthelloConfiguration.OthelloConfig.CHOICE == "t":
            print(f"{Game.p2} passed because they can't move!")
            return "p"
          else:
            return "p",(f"{Game.p2} passed because they can't move!")

    if self.__gamemode.split(" ")[-1] == "AI":
      if self.board.gettotalmoves() == 0:
        if self.__player == Game.p1:
          return "p",(f"The player passed because they couldn't move")
        elif self.__player == Game.p2:
          print(f"The AI passed because they couldn't move!")
          return "p",(f"The AI passed because they couldn't move!")

  def checkwinner(self):


      players = { "w":"White","b":"Black"}

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
        winningplayer = None
        self.__winner = True
        if p1counters > p2counters:
          winningplayer = Game.p1
        if p2counters > p1counters:
          winningplayer = Game.p2
        if p1counters == p2counters:
          winningplayer = "Draw"
      if OthelloConfiguration.OthelloConfig.CHOICE == "t":
        if winningplayer != "Draw":
          print(f"The winner was {players[winningplayer]}!")
        else:
          print("It was a draw!")
        return True
      if OthelloConfiguration.OthelloConfig.CHOICE == "g":
        if winningplayer != "Draw":
          return (f"The winner was {players[winningplayer]}!")
        else:
          return ("It was a draw!")

  def play(self,row,col):
    col -= 1
    row -= 1
    if self.__gamemode == "2 Player":
      if self.board.getboard()[row][col] == Game.move:
        self.board.getboard()[row][col] = self.__player
      else:
        if self.board.getboard()[row][col] != Game.EMPTY:
          print("Place on an empty square!")
          raise Exception
        if self.board.getboard()[row][col] != Game.move:
          print("Can't make that move!")
          raise Exception
    
    if self.__gamemode.split(" ")[-1] == "AI":
      if self.board.getboard()[row][col] == Game.move:
        self.board.getboard()[row][col] = self.__player
      else:
        if self.board.getboard()[row][col] != Game.EMPTY:
          print("Place on an empty square!")
          return -1
        if self.board.getboard()[row][col] != Game.move:
          print("Can't make that move!")
          return -1

  def getplayer(self):
    return self.__player

  def getopposingplayer(self):
    return self.__opposingplayer

  def undomove(self):
    if self.board.undomove(self.__gamemode) != -1:
      if self.__gamemode.split(" ")[-1] != "AI":
        self.switchplayer()
    
    

    




    


      




