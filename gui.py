import tkinter as tk
from Othello import Game
from PIL import ImageTk, Image
from AI import ai
import time
from tkinter import messagebox

class MainWindow(tk.Tk):
  
  def __init__(self):
    super().__init__()
    self.title("Othello")
    self.attributes('-fullscreen',True)
    self.configure(bg="#32a842")

    title = tk.Label(self,text="Othello",bg="#32a842",font=("Arial",25))
    title.place(relx=0.5,rely=0.1,anchor="c")

    frame = tk.Frame(self,bg="#32a842")
    frame.pack(fill="both", expand=True)
    frame.place(relx=0.5,rely=0.55,relwidth=0.2,relheight=0.5,anchor="c")


    playbutton = tk.Button(frame, text="Play", command=self.__mainwindowpressplay,font=("Arial",15),bg="white")
    playbutton.config(height=2)
    playbutton.pack(fill="x",expand=True,anchor=tk.N)


    settingsbutton = tk.Button(frame, text="Settings",font=("Arial",15),bg="white",command=self.__mainwindowsettings)
    settingsbutton.config(height=2)
    settingsbutton.pack(fill="x",expand=True,anchor=tk.E)

    quitbutton = tk.Button(frame, text="Quit", command=self.__quitmainwindow,font=("Arial",15),bg="white")
    quitbutton.config(height=2)
    quitbutton.pack(fill="x",expand=True,anchor=tk.S)

  def __mainwindowpressplay(self):
    pregamewin = PreGameWindow()

  def __mainwindowsettings(self):
    settingswindow = SettingsWindow()

  def __quitmainwindow(self):
    self.destroy()
    self = None


class SettingsWindow():

  def __init__(self):
    self.__window = tk.Toplevel(bg="#32a842")
    self.__window.resizable(True,True)
    self.__window.attributes('-fullscreen',True)

class PreGameWindow():

  def __init__(self):
    self.__window = tk.Toplevel(bg="#32a842")
    self.__window.resizable(True,True)
    self.__window.attributes('-fullscreen',True)

    frame = tk.Frame(self.__window,bg="#32a842")
    frame.pack(fill="both", expand=True)
    frame.place(relx=0.5,rely=0.55,relwidth=0.2,relheight=0.7,anchor="c")

    menu = tk.StringVar()
    menu.set("Select Gamemode")

    drop = tk.OptionMenu(frame, menu,"2 Player","Easy AI")
    drop.pack(fill="x",expand=True,anchor=tk.N)

    startbutton = tk.Button(frame, text="Start",command=lambda: self.__startgame(menu),font=("Arial",15),bg="white")
    startbutton.config(height=2)
    startbutton.pack(fill="x",expand=True,anchor=tk.N)


  def __startgame(self,menu):

    gamemode = menu.get()
    if gamemode == "Select Gamemode":
      tk.messagebox.showerror(title="Warning",message="Select a Gamemode first!")
    else:
      gamewin = GameWindow(gamemode) #Game window created
      self.__window.destroy()
      self.__window = None

      

class GameWindow():

  EMPTY = "_"
  p1 = "⏺"
  p2 = "◯"
  move = "!"

  def Exception():
    pass

  def __init__(self,gamemode):
    self.__game = Game(gamemode,"g")
    self.__window = tk.Toplevel(bg="#32a842")
    self.__window.resizable(True,True)
    self.__window.attributes('-fullscreen',True)
    self.__gamemode = gamemode

    gridbox = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    gridbox.pack(fill="both", expand=True)
    self.__grid = self.__updateGrid(gridbox)
    gridbox.place(relx=0.5,rely=0.5,width=494,height=494,anchor="c")

    backbuttonframe = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    backbuttonframe.pack(side=tk.TOP,anchor="nw")
    backbutton = tk.Button(backbuttonframe,text="Back",command=lambda: self.__backtomain(self.__window),font=("Arial",15))
    backbutton.config(height=1,width=5)
    backbutton.pack()

    blackscoreboardframe = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    blackscoreboardframe.pack(fill="both",expand=True)
    blackscoreboardframe.place(relx=0.22,rely=0.285,width=200,height=100,anchor="c")
    blackscorevalue = tk.StringVar(blackscoreboardframe,self.__game.countercount()[0])
    blackscorepicture = tk.Label(blackscoreboardframe,text="●",font=("Arial",55)).place(relx=0.1)
    blackscorelabel = tk.Label(blackscoreboardframe,textvariable=str(blackscorevalue),font=("Arial",30)).place(relx=0.5,rely=0.25)


    whitescoreboardframe = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    whitescoreboardframe.pack(fill="both",expand=True)
    whitescoreboardframe.place(relx=0.78,rely=0.715,width=200,height=100,anchor="c")
    whitescorevalue = tk.StringVar(whitescoreboardframe,self.__game.countercount()[1])
    whitescorepicture = tk.Label(whitescoreboardframe,text="◯",font=("Arial",24)).place(relx=0.1,rely=0.28)
    whitescorelabel = tk.Label(whitescoreboardframe,textvariable=str(whitescorevalue),font=("Arial",30)).place(relx=0.5,rely=0.25)

    



  def __backtomain(self,window): #Function for deleting going to main menu from game
    window.destroy()
    window = None


  def __updateGrid(self,window): #changes the grid
    self.__game.getpossiblemoves()
    window.columnconfigure(8, weight=1)
    window.columnconfigure(8, weight=1)
    for r in range(len(self.__game.getboard())):
      for c in range(len(self.__game.getboard())):
          cmd = lambda row = r, column = c: self.__turn(row,column,window) 
          f = tk.Frame(window,highlightbackground="black",highlightthickness="2",height=61,width=61)
          squarebutton = tk.Button(f,bg="white",height=1,width=1,command=cmd)
          squarebutton.place(relheight=1,relwidth=1)
          if self.__game.getboard()[r][c] == "b":
            squarebutton.config(text="⏺",font=("Arial",70))
          if self.__game.getboard()[r][c] == "w":
            squarebutton.config(text="◯",font=("Arial",40))
          if self.__game.getboard()[r][c] == "!":
            squarebutton.config(bg="blue")
          f.grid(row=r,column=c)


  def __turn(self,row,column,window): #Placing counter and flipping counters

    row += 1
    column += 1
    if self.__gamemode == "2 Player":
      if self.__game.reviewstate() != "p":
        try:
          self.__game.play(row,column)
          self.__game.flipcounters(row,column,self.__game.getboard())
          self.__game.countercount()
        except:
          pass
        self.__updateGrid(window)
      if self.__game.reviewstate() == "p":
        self.__updateGrid(window)
        self.__game.checkwinner()



    #When a tile is pressed, if the gamemode is AI, play the move, then give the ai a chance to move



    if self.__gamemode.split(" ")[-1] == "AI":


      
      gameai = ai()
      possiblewinner = 0

      #if the player has to pass,

      if self.__game.reviewstate() != "p":
        try:
          if self.__game.play(row,column): 
            return #Give player chance to play again
          else:
            self.__game.flipcounters(row,column,self.__game.getboard())
            self.__game.countercount()     
        except:
          print("something wrong (Player)")
      else:
        self.__updateGrid(window)
        self.__game.checkwinner()


      self.__game.getpossiblemoves()


      if self.__game.reviewstate() != "p":
        try:
          aimove = gameai.getmove(self.__game.getboard(),self.__gamemode.split(" ")[0])
          self.__game.play(aimove[0],aimove[1])
          self.__game.flipcounters(aimove[0],aimove[1],self.__game.getboard())
          self.__game.countercount()
          self.__updateGrid(window)
        except:
          print("something wrong (AI)")
      else:
        self.__updateGrid(window)
        self.__game.checkwinner()



      








    
    


        
