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
  
  def __init__(self):
    self.__game = Game()
    
  def __turn(self):
    while True:
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        if 1 <= row <= 8 and 1 <= col <= 8:
          break
        else:
          print("Enter a number between 1 and 8")
    return row,col

  def run(self):
    print(self.__game)
    row,col = self.__turn()
    try:
      self.__game.play(row,col)
      print(self.__game)
    except:
      pass





    
    


  
  
class Gui(Ui):

  def __init__():
    super().__init__()

