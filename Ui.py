from msilib.schema import Error
from re import A
from Othello import Game
from abc import ABC, abstractmethod


class Ui():

  @abstractmethod
  def run(self):
    raise NotImplementedError

class Terminal(Ui):
  
  def __init__(self):
    self.__game = Game()
    
  def startGame(self):
    pass

  
    
    


  
  
class Gui(Ui):

  def __init__():
    super().__init__()

