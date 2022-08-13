from logging import raiseExceptions
from sys import *
from Ui import Terminal
from Ui import Gui


def start():
  if argv[1] == "g":
    pass
  if argv[1] == "t":
    ui = Terminal()
    ui.run()
  else:
    print("Press 't'to run a game in the terminal and 'g' to run a game in the GUI:")


if __name__ == "__main__":
  if argv[1]:
    start() 
  else:
    print("no")
else:
  print("no")



  

    


