import tkinter as tk
from Othello import Game

class MainWindow(tk.Tk):
  
  def __init__(self):
    super().__init__()
    self.title("Othello")
    self.resizable(True,True)
    #canvas = tk.Canvas(self, height=MainWindow.HEIGHT, width=MainWindow.WIDTH).pack()

    frame = tk.Frame(self, highlightbackground= 'red', highlightthickness=3)
    frame.pack(fill="both", expand=True)
    frame.place(relx=0.5,rely=0.55,relwidth=0.30,relheight=0.5,anchor="c")

    playbutton = tk.Button(frame, text="Play", command=self.__playgame)
    playbutton.pack(fill="x",expand=True,anchor=tk.N)

  def __playgame(self):
    gamewin = tk.Toplevel()

class GameWindow():
  
  def __init__(self):
    tk.Tk()








