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
    while self.__game.result() == None:
      self.__game.getpossiblemoves()
      print(self.__game) #Print the board
      row,col = self.__turn() #Recieve move input
      try:
        self.__game.play(row,col) #Make the move
        self.__game.flip(row,col,self.__game.getboard()) #Flip the counters and remove the possible moves
        self.__game.countercount() #Count and display the counters
      except:
        pass
      
class Gui(Ui):

  def __init__():
    super().__init__()

