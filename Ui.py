from msilib.schema import Error
from re import A
from tempfile import TemporaryFile
from Othello import Game
from abc import ABC, abstractmethod


class Ui():

  @abstractmethod
  def run(self):
    raise NotImplementedError

class Terminal(Ui):
  
  def Exception():
    pass

  def __init__(self):
    self.__game = Game()
    
  def __turn(self): #Requesting the row and column for the next person's move
    while True:
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        if 1 <= row <= 8 and 1 <= col <= 8:
          break
        else:
          print("Enter a number between 1 and 8")
    return row,col

  def run(self): #The continuous run of the game - printing out the board, getting the move, and trying to play the move.
    while True:
      print(self.__game) #Print the board
      row,col = self.__turn() #Recieve move input
      try:
        self.__game.play(row,col) #Make the move
        self.__game.flip(row,col)
      except:
        pass
      
class Gui(Ui):

  def __init__():
    super().__init__()

