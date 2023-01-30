from Ui import Terminal, Gui

class OthelloConfig:

  CHOICE = None

  def __init__(self):
    pass

  def run(self,choice):
    OthelloConfig.CHOICE = choice
    if choice == "t":
      self.ui = Terminal()
    if choice == "g":
      self.ui = Gui()
    self.ui.run()

  

