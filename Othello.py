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
    

 
 
  def __repr__(self):
    output = "\n  " + " ".join(str(i+1) for i in range(8))
    for row in range(8):
      output = output + "\n" + str(row+1) + " " + " ".join(self.board.getBoard()[row][i] for i in range(8))
    output = output + "\n" + (f"{self.__player}'s turn: ")
    return output



  def switchPlayer(self):
    if self.__player == Game.p1: 
      self.__player = Game.p2
      self.__opposingplayer = Game.p1
    else:
      self.__player = Game.p1
      self.__opposingplayer = Game.p2






  def reviewState(self):
    if self.__gamemode == "2 Player":
      if self.board.getTotalMoves() == 0:
        if self.__player == Game.p1:
          print("p1 pass")
        else:
          print("p2 pass")
        self.switchPlayer()
        return "p"

    if self.__gamemode.split(" ")[-1] == "AI":
      if self.board.getTotalMoves() == 0:
        return "p"


  def checkWinner(self):

      freeSpaces = 0
      p1counters = 0
      p2counters = 0
      for a in range(8):
        for b in range(8):
          space = self.board.getBoard()[a][b]
          if space == Game.p1:
            p1counters += 1
          if space == Game.p2:
            p2counters += 1
          if space == Game.EMPTY or space == Game.move:
            freeSpaces += 1

      if self.__gamemode.split(" ")[-1] == "AI":
        self.switchPlayer()


      if freeSpaces == 0 or self.reviewState() == "p":
        winningPlayer = None
        if p1counters > p2counters:
          winningPlayer = Game.p1
        if p2counters > p1counters:
          winningPlayer = Game.p2
        if p1counters == p2counters:
          winningPlayer = "Draw"
        if OthelloConfiguration.OthelloConfig.CHOICE == "t":
          if winningPlayer != "Draw":
            print(f"The winner was {winningPlayer}!")
            return True
          else:
            print("It was a draw!")
          
        if OthelloConfiguration.OthelloConfig.CHOICE == "g":
          if winningPlayer != "Draw":
            if winningPlayer == Game.p2:
              if self.__gamemode.split(" ")[-1] == "AI":
                return True, ("The AI wins!")
              else:
                return True, (f"The winner was White!")
            if winningPlayer == Game.p1:
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
      if self.board.getBoard()[row][col] == Game.move:
        self.board.getBoard()[row][col] = self.__player
      else:
        if self.board.getBoard()[row][col] != Game.EMPTY:
          if OthelloConfiguration.OthelloConfig.CHOICE == "t":
            print("Place on an empty square!")
            raise Exception
          else:
            return "EmptySquare"
        if self.board.getBoard()[row][col] != Game.move:
          if OthelloConfiguration.OthelloConfig.CHOICE == "t":
            print("Can't make that move!")
            raise Exception
          else:
            return "InvalidMove"
    
    if self.__gamemode.split(" ")[-1] == "AI":
      if self.board.getBoard()[row][col] == Game.move:
        self.board.getBoard()[row][col] = self.__player
      else:
        if self.board.getBoard()[row][col] != Game.EMPTY:
          return "EmptySquare"
        if self.board.getBoard()[row][col] != Game.move:
          return "InvalidMove"

  def getplayer(self):
    return self.__player

  def getOpposingPlayer(self):
    return self.__opposingplayer

  def undoMove(self):
    if self.board.undoMove(self.__gamemode) != -1:
      if self.__gamemode.split(" ")[-1] != "AI":
        self.switchPlayer()
    
    

    




    


      




