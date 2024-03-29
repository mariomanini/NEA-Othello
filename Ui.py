from Othello import Game
from abc import ABC, abstractmethod
import tkinter as tk
from Gui import MainWindow



class Ui():

  @abstractmethod
  def run(self):
    raise NotImplementedError

class Terminal(Ui):
  
  def Exception():
    pass

  def __init__(self):
    self.__game = Game("2 Player")
    
  def __turn(self): #Requesting the row and column for the next person's move
    while True:
      while True:
        try:
          row = int(input("Enter row: "))
          col = int(input("Enter col: "))
          break
        except ValueError:
          print("Enter an integer...")
          continue
      if 1 <= row <= 8 and 1 <= col <= 8:
        break
      else:
        print("Enter a number between 1 and 8")
    return row,col  

  def run(self): #The continuous run of the game - printing out the board, getting the move, and trying to play the move.
    while True:
      self.__game.board.getPossibleMoves(self.__game.getplayer(),self.__game.getOpposingPlayer()) #Add the move tiles
      print(self.__game) #Print the board
      self.__game.reviewState() #Che ck if there is a pass to be made
      if self.__game.reviewState() != "p": 
        row,col = self.__turn() #Recieve move input
        try:
          self.__game.play(row,col) #Make the move
          self.__game.board.flipCounters(row,col,self.__game.getplayer())
          self.__game.switchPlayer() #Flip the counters and remove the possible moves
          self.__game.board.counterCount() #Count and display the counters
        except:
          pass
      else:
        if self.__game.checkWinner() == True:
          break
          

class Gui(Ui):

  def Exception():
    pass

  def __init__(self):
    pass


  def run(self):
    mainwindow = MainWindow()
    mainwindow.mainloop()





      











