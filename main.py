from sys import *
from Ui import Terminal
from Ui import Gui

def start():
  print("Press 't'to run a game in the terminal and 'g' to run a game in the GUI:")
  print(argv[1])
  if argv[1] == "g":
    pass
  if argv[1] == "t":
    newgame = Terminal()

if __name__ == "__main__":
  start()
else:
  print("no")
  

    


