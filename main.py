
from logging import raiseExceptions
from sys import *
from Ui import Terminal
from Ui import Gui


def start():
  try:
    if argv[1]:
      if argv[1] == "g":
        ui = Gui()
        ui.run()
      if argv[1] == "t":
        ui = Terminal()
        ui.run()
  except:
    choice = input("Input 't'to run a game in the terminal and 'g' to run a game in the GUI: ")
    if choice == "t":
      ui = Terminal()
      ui.run()
    if choice == "g":
      ui = Gui()
      ui.run()

if __name__ == "__main__":
  start()
else:
  print("not working")
  






  

    


