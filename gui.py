import tkinter as tk
from Othello import Game
from PIL import ImageTk, Image
import time
from tkinter import messagebox
from AIEngine import AIEngine



class MainWindow(tk.Tk):

  COLOUR = "green"
  SHOWPOSSIBLEMOVES = True
  
  
  def __init__(self):
    super().__init__()
    self.title("Othello")
    self.attributes('-fullscreen',True)
    self.configure(bg=MainWindow.COLOUR)

    title = tk.Label(self,text="Othello",bg=MainWindow.COLOUR,font=("Helvetica",25))
    title.place(relx=0.5,rely=0.1,anchor="c")

    frame = tk.Frame(self,bg=MainWindow.COLOUR)
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

  def updatetogglecountersettings(self,toggle):
    if toggle == True:
      self.SHOWPOSSIBLEMOVES = True
    if toggle == False:
      self.SHOWPOSSIBLEMOVES = False

class SettingsWindow(MainWindow):

  def __init__(self):
    self.__window = tk.Toplevel(bg=MainWindow.COLOUR)
    self.__window.resizable(True,True)
    self.__window.attributes('-fullscreen',True)

    frame = tk.Frame(self.__window,bg=MainWindow.COLOUR)
    frame.pack(fill="both", expand=True)
    frame.place(relx=0.5,rely=0.55,relwidth=0.2,relheight=0.7,anchor="c")

    togglecounters = tk.StringVar()
    togglecounters.set("Toggle move hint")

    countermenu = tk.OptionMenu(frame,togglecounters,"Show possible moves","Don't Show Possible Moves")
    countermenu.config(height=2)
    countermenu.pack(fill="x",expand=True,anchor=tk.E)

    backbuttonframe = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    backbuttonframe.pack(side=tk.TOP,anchor="nw")
    backbutton = tk.Button(backbuttonframe,text="Back",command=lambda: self.__backtomain(self.__window,togglecounters),font=("Arial",15))
    backbutton.config(height=1,width=5)
    backbutton.pack()

  def __backtomain(self,window,togglecounteroption):
    self.__updatesettings(togglecounteroption)
    window.destroy()
    window = None

  def __updatesettings(self,togglecounteroption):
    toggle = togglecounteroption.get()
    if toggle == "Show Possible Moves" or toggle == "Toggle move hint":
      MainWindow.updatetogglecountersettings(MainWindow,True)
    if toggle == "Don't Show Possible Moves": 
      MainWindow.updatetogglecountersettings(MainWindow,False)
    return


class PreGameWindow(MainWindow):

  def __init__(self):
    self.__window = tk.Toplevel(bg=MainWindow.COLOUR)
    self.__window.resizable(True,True)
    self.__window.attributes('-fullscreen',True)

    frame = tk.Frame(self.__window,bg=MainWindow.COLOUR)
    frame.pack(fill="both", expand=True)
    frame.place(relx=0.5,rely=0.55,relwidth=0.2,relheight=0.7,anchor="c")

    menu = tk.StringVar()
    menu.set("Select Gamemode")

    drop = tk.OptionMenu(frame, menu,"2 Player","Easy AI","Medium AI")
    drop.config(height=2)
    drop.pack(fill="x",expand=True,anchor=tk.E)

    startbutton = tk.Button(frame, text="Start",command=lambda: self.__startgame(menu),font=("Arial",15),bg="white")
    startbutton.config(height=2)
    startbutton.pack(fill="x",expand=True,anchor=tk.N)

    backbuttonframe = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    backbuttonframe.pack(side=tk.TOP,anchor="nw")
    backbutton = tk.Button(backbuttonframe,text="Back",command=lambda: self.__backtomain(self.__window),font=("Arial",15))
    backbutton.config(height=1,width=5)
    backbutton.pack()

  
  def __backtomain(self,window):
    window.destroy()
    window = None


  def __startgame(self,menu):

    gamemode = menu.get()
    if gamemode == "Select Gamemode":
      tk.messagebox.showerror(title="Warning",message="Select a Gamemode first!")
    else:
      gamewin = GameWindow(gamemode) #Game window created
      self.__window.destroy()
      self.__window = None

      

class GameWindow(MainWindow):

  EMPTY = "_"
  p1 = "⏺"
  p2 = "◯"
  move = "!"



  def Exception():
    pass

  def __init__(self,gamemode):
    self.__togglecounters = MainWindow.SHOWPOSSIBLEMOVES
    self.__game = Game(gamemode)
    self.__window = tk.Toplevel(bg=MainWindow.COLOUR)
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

    undobuttonframe = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    undobuttonframe.pack(side=tk.BOTTOM,anchor="ne")
    undobutton = tk.Button(undobuttonframe,text="Undo",command=lambda: self.__undo(gridbox),font=("Arial",15))
    undobutton.config(height=1,width=5)
    undobutton.pack()

    self.__updateScore()



  def __backtomain(self,window): #Function for deleting going to main menu from game
    window.destroy()
    window = None


  def __updateScore(self):

    blackscoreboardframe = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    blackscoreboardframe.pack(fill="both",expand=True)
    blackscoreboardframe.place(relx=0.22,rely=0.285,width=200,height=100,anchor="c")
    blackscorevalue = tk.StringVar(blackscoreboardframe,self.__game.board.countercount()[0])
    blackscorepicture = tk.Label(blackscoreboardframe,text="●",font=("Arial",55)).place(relx=0.1)
    blackscorelabel = tk.Label(blackscoreboardframe,textvariable=str(blackscorevalue),font=("Arial",30)).place(relx=0.5,rely=0.25)

    whitescoreboardframe = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    whitescoreboardframe.pack(fill="both",expand=True)
    whitescoreboardframe.place(relx=0.78,rely=0.715,width=200,height=100,anchor="c")
    whitescorevalue = tk.StringVar(whitescoreboardframe,self.__game.board.countercount()[1])
    whitescorepicture = tk.Label(whitescoreboardframe,text="◯",font=("Arial",24)).place(relx=0.1,rely=0.28)
    whitescorelabel = tk.Label(whitescoreboardframe,textvariable=str(whitescorevalue),font=("Arial",30)).place(relx=0.5,rely=0.25)

    if self.__game.getplayer() == self.__game.p1:
      try:
        whitescoreboardframe.config(highlightbackground="black")
      except:
        pass
      blackscoreboardframe.config(highlightbackground="red")
    else:
      try:
        blackscoreboardframe.config(highlightbackground="black")
      except:
        pass
      whitescoreboardframe.config(highlightbackground="#ADD8E6")
      
    
  def __updateGrid(self,window): #changes the grid
    self.__game.board.getpossiblemoves(self.__game.getplayer(),self.__game.getopposingplayer())
    window.columnconfigure(8, weight=1)
    window.columnconfigure(8, weight=1)
    for r in range(len(self.__game.board.getboard())):
      for c in range(len(self.__game.board.getboard())):
          cmd = lambda row = r, column = c: self.__turn(row,column,window) 
          f = tk.Frame(window,highlightbackground="black",highlightthickness="2",height=61,width=61)
          squarebutton = tk.Button(f,bg="white",height=1,width=1,command=cmd)
          squarebutton.place(relheight=1,relwidth=1)
          if self.__game.board.getboard()[r][c] == "b":
            squarebutton.config(text="⏺",font=("Arial",70))
          if self.__game.board.getboard()[r][c] == "w":
            squarebutton.config(text="◯",font=("Arial",40))
          if self.__togglecounters == True:
            if self.__game.board.getboard()[r][c] == "!":
              if self.__game.getplayer() == "w":
                squarebutton.config(bg="#ADD8E6")
              elif self.__game.getplayer() == "b":
                squarebutton.config(bg="red")
          f.grid(row=r,column=c)
    self.__updateScore()


  def __turn(self,row,column,window): #Placing counter and flipping counters
    row += 1
    column += 1
    if self.__gamemode == "2 Player":
      if self.__game.reviewstate() != "p":
        try:
          self.__game.play(row,column)
          self.__game.board.flipcounters(row,column,self.__game.getplayer())
          self.__game.switchplayer()
          self.__game.countercount()
        except:
          pass
        self.__updateGrid(window)
      if self.__game.reviewstate() == "p":
        self.__updateGrid(window)
        self.__game.checkwinner()



    #When a tile is pressed, if the gamemode is AI, play the move, then give the ai a chance to move



    if self.__gamemode.split(" ")[-1] == "AI":
      possiblewinner = 0
      if self.__game.reviewstate() != "p":
        try:
          if self.__game.play(row,column): 
            return #Give player chance to play again
          else:
            self.__game.board.flipcounters(row,column,self.__game.getplayer())
            self.__game.switchplayer()
            self.__game.board.countercount()     
        except:
          print("something wrong (Player)")
      else:
        self.__updateGrid(window)
        self.__game.checkwinner()
      self.__game.board.getpossiblemoves(self.__game.getplayer(),self.__game.getopposingplayer())


      if self.__game.reviewstate() != "p":
        try:
          aiEngine = AIEngine(self.__gamemode.split(" ")[0])
          aimove = aiEngine.getBestMove(self.__game.board)
          self.__game.play(aimove[0],aimove[1])
          self.__game.board.flipcounters(aimove[0],aimove[1],self.__game.getplayer())
          self.__game.switchplayer()
          self.__game.board.countercount()
          self.__updateGrid(window)
        except:
          print("something wrong (AI)")
      else:
        self.__updateGrid(window)
        self.__game.checkwinner()




  def __undo(self,window):
    self.__game.undomove()
    self.__updateGrid(window)      








    
    


        
