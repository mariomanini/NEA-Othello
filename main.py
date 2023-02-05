
from logging import raiseExceptions
from sys import *
import OthelloConfiguration


def start():

  try:
    if argv[1]:
      config.run(argv[1])
  except:
    choice = -1
    while choice != "t" or choice != "g":
      choice = input("Input 't' to run a game in the terminal and 'g' to run a game in the GUI: ")
      config.run(choice)


if __name__ == "__main__":
  config = OthelloConfiguration.OthelloConfig()
  start()













    


