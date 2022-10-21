import tkinter as tk
from xml.etree.ElementTree import TreeBuilder
from Othello import Game
from PIL import ImageTk, Image

class MainWindow(tk.Tk):
  
  def __init__(self):
    super().__init__()
    self.title("Othello")
    self.attributes('-fullscreen',True)
    self.configure(bg="#32a842")

    title = tk.Label(self,text="Othello",font=("Arial",25))
    title.place(relx=0.5,rely=0.1,anchor="c")

    frame = tk.Frame(self,bg="#32a842")
    frame.pack(fill="both", expand=True)
    frame.place(relx=0.5,rely=0.55,relwidth=0.2,relheight=0.5,anchor="c")


    playbutton = tk.Button(frame, text="Play", command=self.__mainwindowpressplay,font=("Arial",15),bg="white")
    playbutton.config(height=2)
    playbutton.pack(fill="x",expand=True,anchor=tk.N)


    settingsbutton = tk.Button(frame, text="Settings",font=("Arial",15),bg="white")
    settingsbutton.config(height=2)
    settingsbutton.pack(fill="x",expand=True,anchor=tk.E)

    quitbutton = tk.Button(frame, text="Quit", command=self.__quitmainwindow,font=("Arial",15),bg="white")
    quitbutton.config(height=2)
    quitbutton.pack(fill="x",expand=True,anchor=tk.S)

  def __mainwindowpressplay(self):
    gamewin = GameWindow()

  def __quitmainwindow(self):
      self.destroy()
      self = None

class GameWindow():

  

  def __init__(self):
    self.__game = Game()
    self.__window = tk.Toplevel(bg="#32a842")
    self.__window.resizable(True,True)
    self.__window.attributes('-fullscreen',True)

    gridbox = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    gridbox.pack(fill="both", expand=True)
    self.__grid = self.__createGrid(gridbox)
    gridbox.place(relx=0.5,rely=0.5,width=494,height=494,anchor="c")

    backbuttonframe = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    backbuttonframe.pack(side=tk.TOP,anchor="nw")
    backbutton = tk.Button(backbuttonframe,text="Back",command=lambda: self.__backtomain(self.__window),font=("Arial",15))
    backbutton.config(height=1,width=5)
    backbutton.pack()


  def __backtomain(self,window):
    window.destroy()
    window = None



  def __createGrid(self,window):
    
    window.columnconfigure(8, weight=1)
    window.columnconfigure(8, weight=1)
    for r in range(len(self.__game.getboard())):
      for c in range(len(self.__game.getboard())):
          cmd = lambda row = r, column = c: self.__ButtonPress(row,column) 
          f = tk.Frame(window,highlightbackground="black",highlightthickness="2",height=61,width=61)
          squarebutton = tk.Button(f,bg="white",height=1,width=1,command=cmd)
          squarebutton.place(relheight=1,relwidth=1)
          if (r == 4 and c == 4) or (r == 3 and c == 3):
            squarebutton.config(text="⏺",font=("Arial",70))
          if (r == 3 and c == 4) or (r == 4 and c == 3):
            squarebutton.config(text="◯",font=("Arial",40))

          f.grid(row=r,column=c)


  def __ButtonPress(self,row,column):
    print(f"{row},{column}")
    return row,column

  def __playgame(self):
    while True:
      self.__game.play(self.__ButtonPress)
  

          #squarebutton.pack(fill="both")
            #startsquarep1.place(anchor="c")

          #squarebutton.pack(expand=True)



        
