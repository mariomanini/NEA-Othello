import tkinter as tk
from Othello import Game
from PIL import ImageTk, Image
import time
from tkinter import messagebox
from AIEngine import AIEngine
from time import sleep



class MainWindow(tk.Tk):

  COLOUR = "green"
  SHOWPOSSIBLEMOVES = True
  
  def __init__(self):
    super().__init__()
    self.title("Othello")
    self.attributes('-fullscreen',True)
    self.configure(bg=MainWindow.COLOUR)
    
    title = tk.Label(self,text="Othello",bg=MainWindow.COLOUR,font=("Helvetica",35))
    title.place(relx=0.5,rely=0.15,anchor="c")

    frame = tk.Frame(self,bg=MainWindow.COLOUR)
    frame.pack(fill="both", expand=True)
    frame.place(relx=0.5,rely=0.55,relwidth=0.2,relheight=0.5,anchor="c")


    playButton = tk.Button(frame, text="Play", command=self.__mainWindowPressPlay,font=("Arial",15),bg="white")
    playButton.config(height=2)
    playButton.pack(fill="x",expand=True,anchor=tk.N)

    settingsButton = tk.Button(frame, text="Settings",font=("Arial",15),bg="white",command=self.__mainWindowSettings)
    settingsButton.config(height=2)
    settingsButton.pack(fill="x",expand=True,anchor=tk.E)

    rulesButton = tk.Button(frame,text="Rules",command=self.__mainWindowRules,font=("Arial",15),bg="white")
    rulesButton.config(height=2)
    rulesButton.pack(fill="x",expand=True,anchor=tk.E)

    quitButton = tk.Button(frame, text="Quit", command=self.__quitMainWindow,font=("Arial",15),bg="white")
    quitButton.config(height=2)
    quitButton.pack(fill="x",expand=True,anchor=tk.S)



  def __mainWindowRules(self):
    rulesWindow()

  def __mainWindowPressPlay(self):
    PreGameWindow()

  def __mainWindowSettings(self):
    SettingsWindow()

  def __quitMainWindow(self):
    self.destroy()
    self = None

  def updateColourSettings(self,colour):
    MainWindow.COLOUR = colour

  def updateToggleCounterSettings(self,toggle):
    if toggle == True:
      self.SHOWPOSSIBLEMOVES = True
    if toggle == False:
      self.SHOWPOSSIBLEMOVES = False

class rulesWindow(MainWindow):

  def __init__(self):
    self.__window = tk.Toplevel(bg=MainWindow.COLOUR)
    self.__window.resizable(True,True)
    self.__window.attributes('-fullscreen',True)

    frame = tk.Frame(self.__window,bg=MainWindow.COLOUR)
    frame.pack(fill="both", expand=True)
    frame.place(relx=0.5,rely=0.55,relwidth=0.25,relheight=0.7,anchor="c")

    backButtonFrame = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    backButtonFrame.pack(side=tk.TOP,anchor="nw")
    backButton = tk.Button(backButtonFrame,text="Back",command=lambda: self.__backToMain(self.__window),font=("Arial",15))
    backButton.config(height=1,width=5)
    backButton.pack()



    rules = tk.Message(frame,text="Othello is a two player board game played on an 8x8 grid. Each\
 player has 32 black or white counters and take turns placing counters one at a time on the board. The aim of the game is to \
have the most counters of your colour on the board by the time the game ends. A game “ends” when either player is unable to \
make a valid move or when the board is filled. To see how the moves work, play the tutorial below.",bg="White",anchor=tk.N,justify="center",font=("Helevetica",14))
    rules.pack(anchor=tk.N)

    tutorialButton = tk.Button(frame,text="Play Tutorial",command=lambda: self.__playTutorial(self.__window))
    tutorialButton.config(height=2)
    tutorialButton.pack(fill="x",anchor=tk.S,pady=15)

  def __backToMain(self,window):
    window.destroy()
    window = None

  def __playTutorial(self,window):
    window.destroy()
    window = None
    tutorialWindow()

class tutorialWindow(MainWindow):

  def __init__(self):
    self.__window = tk.Toplevel(bg=MainWindow.COLOUR)
    self.__window.resizable(True,True)
    self.__window.attributes('-fullscreen',True)
    
    gridBox = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    gridBox.pack(fill="both", expand=True)
    self.__game = Game("2 Player")
    self.__updateGrid(gridBox,True)
    gridBox.place(relx=0.5,rely=0.5,width=494,height=494,anchor="c")

    self.__messagesFrame = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    self.__messagesFrame.pack(fill="both",expand=True)
    self.__messagesFrame.place(relx=0.5,rely=0.18,width=494,height=50,anchor="c")

    self.__message = tk.Label(self.__messagesFrame,text="This is the starting board in Othello, \
the red squares indicate where you can play. \nTry to place a counter on one of the red squares.",font=("Helevetica",10))
    self.__message.pack(fill="x")

    backButtonFrame = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    backButtonFrame.pack(side=tk.TOP,anchor="nw")
    backButton = tk.Button(backButtonFrame,text="Back",command=lambda: self.__backToMain(self.__window),font=("Arial",15))
    backButton.config(height=1,width=5)
    backButton.pack()


  
  def __updateGrid(self,window,showCounters):

    self.__game.board.getPossibleMoves(self.__game.getplayer(),self.__game.getOpposingPlayer())
    window.columnconfigure(8, weight=1)
    window.columnconfigure(8, weight=1)
    for r in range(8):
      for c in range(8):

        cmd2 = lambda row = r, column = c: self.__finalTutorial(row,column,window) 
        cmd = lambda row = r, column = c: self.__nextTutorial(row,column,window) 
        f = tk.Frame(window,highlightbackground="black",highlightthickness="2",height=61,width=61)
        if showCounters == True:
          squarebutton = tk.Button(f,bg="white",height=1,width=1,command=cmd)
        if showCounters == False:
          squarebutton = tk.Button(f,bg="white",height=1,width=1,command=cmd2)
        if showCounters == "Finish":
          squarebutton = tk.Button(f,bg="white",height=1,width=1,command=cmd)
          squarebutton.config(state=tk.DISABLED)
        squarebutton.place(relheight=1,relwidth=1)
        f.grid(row=r,column=c)
        if self.__game.board.getBoard()[r][c] == "b":
          squarebutton.config(text="⏺",font=("Arial",70))
        if self.__game.board.getBoard()[r][c] == "w":
          squarebutton.config(text="◯",font=("Arial",40))
        if self.__game.board.getBoard()[r][c] == "!" and showCounters == True: 
          if self.__game.getplayer() == "w":
            squarebutton.config(bg="#ADD8E6")
          elif self.__game.getplayer() == "b":
            squarebutton.config(bg="red")

  def __nextTutorial(self,row,column,window):
    row += 1
    column += 1
    
    self.__game.play(row,column)
    self.__game.board.flipCounters(row,column,self.__game.getplayer())
    self.__game.switchPlayer()
    self.__game.board.counterCount()
    self.__updateGrid(window,False)
    self.__updateMessage("You flippepd over a counter since it was outflanked by your own counter! \nNow it is white's turn. Try to play a move without any help.",8)


  def __finalTutorial(self,row,column,window):
    row += 1
    column += 1
    
    self.__game.play(row,column)
    self.__game.board.flipCounters(row,column,self.__game.getplayer())
    self.__game.switchPlayer()
    self.__game.board.counterCount()
    self.__updateGrid(window,False)

    self.__updateMessage("Well done! Now try to play a proper game!",12)
    self.__updateGrid(window,"Finish")

  def __updateMessage(self,message,size):
    self.__message.config(text=message,font=("Helevetica",size))
      
  def __backToMain(self,window):
    window.destroy()
    window = None


class SettingsWindow(MainWindow):

  def __init__(self):
    self.__window = tk.Toplevel(bg=MainWindow.COLOUR)
    self.__window.resizable(True,True)
    self.__window.attributes('-fullscreen',True)

    frame = tk.Frame(self.__window,bg=MainWindow.COLOUR)
    frame.pack(fill="both", expand=True)
    frame.place(relx=0.5,rely=0.55,relwidth=0.2,relheight=0.7,anchor="c")

    toggleCounters = tk.StringVar()
    toggleCounters.set("Toggle move hint")

    counterMenu = tk.OptionMenu(frame,toggleCounters,"Show Possible Moves","Don't Show Possible Moves")
    counterMenu.config(height=2)
    counterMenu.pack(fill="x",expand=True,anchor=tk.E)

    customColour = tk.StringVar()
    customColour.set("Colour Settings")

    colourMenu = tk.OptionMenu(frame,customColour,"Default","Dark Mode","Light Mode")
    colourMenu.config(height=2)
    colourMenu.pack(fill="x",expand=True,anchor=tk.N)

    backButtonFrame = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    backButtonFrame.pack(side=tk.TOP,anchor="nw")
    backButton = tk.Button(backButtonFrame,text="Back",command=lambda: self.__backToMain(self.__window,toggleCounters,customColour),font=("Arial",15))
    backButton.config(height=1,width=5)
    backButton.pack()

  def __backToMain(self,window,toggleCounterOption,colourOption):
    self.__updateSettings(toggleCounterOption,colourOption)
    window.destroy()
    window = None

  def __updateSettings(self,toggleCounterOption,colourOption):
    toggle = toggleCounterOption.get()
    if toggle == "Show Possible Moves" or toggle == "Toggle move hint":
      MainWindow.updateToggleCounterSettings(MainWindow,True)
    if toggle == "Don't Show Possible Moves": 
      MainWindow.updateToggleCounterSettings(MainWindow,False)
    colour = colourOption.get()
    if colour == "Colour Settings" or colour == "Default":
      MainWindow.updateColourSettings(MainWindow,"green")
    if colour == "Light Mode":
      MainWindow.updateColourSettings(MainWindow,"white")
    if colour == "Dark Mode":
      MainWindow.updateColourSettings(MainWindow,"black")
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

    drop = tk.OptionMenu(frame, menu,"2 Player","Easy AI","Medium AI","Hard AI")
    drop.config(height=2)
    drop.pack(fill="x",expand=True,anchor=tk.E)

    startButton = tk.Button(frame, text="Start",command=lambda: self.__startGame(menu),font=("Arial",15),bg="white")
    startButton.config(height=2)
    startButton.pack(fill="x",expand=True,anchor=tk.N)

    backButtonFrame = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    backButtonFrame.pack(side=tk.TOP,anchor="nw")
    backButton = tk.Button(backButtonFrame,text="Back",command=lambda: self.__backToMain(self.__window),font=("Arial",15))
    backButton.config(height=1,width=5)
    backButton.pack()

  
  def __backToMain(self,window):
    window.destroy()
    window = None


  def __startGame(self,menu):
    gamemode = menu.get()
    if gamemode == "Select Gamemode":
      tk.messagebox.showerror(title="Warning",message="Select a Gamemode first!")
    else:
      GameWindow(gamemode)
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
    self.__toggleCounters = MainWindow.SHOWPOSSIBLEMOVES
    self.__game = Game(gamemode)
    self.__window = tk.Toplevel(bg=MainWindow.COLOUR)
    self.__window.resizable(True,True)
    self.__window.attributes('-fullscreen',True)
    self.__gamemode = gamemode

    gridBox = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    gridBox.pack(fill="both", expand=True)
    self.__updateGrid(gridBox)
    gridBox.place(relx=0.5,rely=0.5,width=494,height=494,anchor="c")

    backButtonFrame = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    backButtonFrame.pack(side=tk.TOP,anchor="nw")
    backButton = tk.Button(backButtonFrame,text="Back",command=lambda: self.__backToMain(self.__window),font=("Arial",15))
    backButton.config(height=1,width=5)
    backButton.pack()

    undoButtonFrame = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    undoButtonFrame.place(anchor="c",relx=0.5,rely=0.8)
    self.__undoButton = tk.Button(undoButtonFrame,text="Undo",command=lambda: self.__undo(gridBox),font=("Arial",15))
    self.__undoButton.config(height=1,width=5)
    self.__undoButton.pack()

    if self.__gamemode.split(" ")[-1] == "AI":
      hintButtonFrame = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
      hintButtonFrame.place(anchor="c",relx=0.43,rely=0.8)
      self.__hintButton = tk.Button(hintButtonFrame,text="Hint",command=lambda: self.__hint(gridBox),font=("Arial",15))
      self.__hintButton.config(height=1,width=5)
      self.__hintButton.pack()

    self.__messagesFrame = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    self.__messagesFrame.pack(fill="both",expand=True)
    self.__messagesFrame.place(relx=0.5,rely=0.18,width=494,height=50,anchor="c")

    self.__passMessage = tk.Label(self.__messagesFrame)
    self.__passMessage.place(anchor="c",relx=0.5,rely=0.5)

    self.__updateScore()

  def __backToMain(self,window): 
    window.destroy()
    window = None


  def __updateScore(self):

    blackScoreboardFrame = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    blackScoreboardFrame.pack(fill="both",expand=True)
    blackScoreboardFrame.place(relx=0.22,rely=0.285,width=200,height=100,anchor="c")
    blackScoreValue = tk.StringVar(blackScoreboardFrame,self.__game.board.counterCount()[0])
    blackScorePicture = tk.Label(blackScoreboardFrame,text="●",font=("Arial",55)).place(relx=0.1)
    blackScoreLabel = tk.Label(blackScoreboardFrame,textvariable=str(blackScoreValue),font=("Arial",30)).place(relx=0.5,rely=0.25)

    whiteScoreBoardFrame = tk.Frame(self.__window,highlightbackground="black",highlightthickness="3")
    whiteScoreBoardFrame.pack(fill="both",expand=True)
    whiteScoreBoardFrame.place(relx=0.78,rely=0.715,width=200,height=100,anchor="c")
    whiteScoreValue = tk.StringVar(whiteScoreBoardFrame,self.__game.board.counterCount()[1])
    whiteScorePicture = tk.Label(whiteScoreBoardFrame,text="◯",font=("Arial",24)).place(relx=0.1,rely=0.28)
    whiteScoreLabel = tk.Label(whiteScoreBoardFrame,textvariable=str(whiteScoreValue),font=("Arial",30)).place(relx=0.5,rely=0.25)

    if self.__game.getplayer() == self.__game.p1:
      try:
        whiteScoreBoardFrame.config(highlightbackground="black")
      except:
        pass
      blackScoreboardFrame.config(highlightbackground="red")
    else:
      try:
        blackScoreboardFrame.config(highlightbackground="black")
      except:
        pass
      whiteScoreBoardFrame.config(highlightbackground="#ADD8E6")
      
    
  def __updateGrid(self,window,AImove=None,hint=None):

    showHint = False
    if hint != None:
      hintRow = int(hint[0]) - 1
      hintCol = int(hint[-1]) -1
      showHint = True

    #If the computer has made a move, display it on the grid.

    showAImove = False
    if AImove != None: 
      aiRow = int(AImove[0]) - 1
      aiCol = int(AImove[-1]) - 1
      showAImove = True

    if showHint == False:
      self.__game.board.getPossibleMoves(self.__game.getplayer(),self.__game.getOpposingPlayer())
    window.columnconfigure(8, weight=1)
    window.columnconfigure(8, weight=1)
    for r in range(len(self.__game.board.getBoard())):
      for c in range(len(self.__game.board.getBoard())):
          cmd = lambda row = r, column = c: self.__turn(row,column,window) 
          f = tk.Frame(window,highlightbackground="black",highlightthickness="2",height=61,width=61)
          squarebutton = tk.Button(f,bg="white",height=1,width=1,command=cmd)
          squarebutton.place(relheight=1,relwidth=1)
          if self.__game.board.getBoard()[r][c] == "b":
            squarebutton.config(text="⏺",font=("Arial",70))
          if self.__game.board.getBoard()[r][c] == "w":
            squarebutton.config(text="◯",font=("Arial",40))    
          if showAImove == True:
            if r == aiRow and c == aiCol:
              squarebutton.config(bg="yellow")
          if self.__toggleCounters == True:
            if self.__game.board.getBoard()[r][c] == "!":
              if self.__game.getplayer() == "w":
                squarebutton.config(bg="#ADD8E6")
              elif self.__game.getplayer() == "b":
                squarebutton.config(bg="red")
          if showHint == True:
            if r == hintRow and c == hintCol:
              squarebutton.config(bg="green")    
          f.grid(row=r,column=c)
    self.__updateScore()

  #This function will run every time a cell is pressed in the GUI.

  def __turn(self,row,column,window):

    #// GROUP B SKILL - DICTIONARIES//

    players = {"w":"White","b":"Black"}
    
    row += 1
    column += 1

    if self.__gamemode == "2 Player":

      #If the player is able to make a move:

      if self.__game.reviewState() != "p":


        #Display a message if the user makes an error.

        if self.__game.play(row,column) == "EmptySquare":
          self.__displayMessage("Place on an Empty Square!")

          #Return to allow them to play again

          return
        elif self.__game.play(row,column) == "InvalidMove":
          self.__displayMessage("Can't make that move!")
          return
        else:
          self.__displayMessage("")

          #Flip the counters after the move has been made.

          self.__game.board.flipCounters(row,column,self.__game.getplayer())
          self.__game.switchPlayer()
          self.__game.board.counterCount()

        self.__updateGrid(window)

        #Display the winner if there is one.

        if self.__game.checkWinner()[0] == True:
          self.__displayMessage(self.__game.checkWinner()[1])
          self.__freezeButtons()
      else:
        self.__displayMessage(f"{players[self.__game.getOpposingPlayer()]} has passed!")
        self.__updateGrid(window)

    #The turn system for playing asgainst the computer.

    if self.__gamemode.split(" ")[-1] == "AI":
      if self.__game.reviewState() != "p":
        if self.__game.play(row,column) == "EmptySquare":
          self.__displayMessage("Place on an Empty Square!")
          return
        elif self.__game.play(row,column) == "InvalidMove":
          self.__displayMessage("Can't make that move!")
          return
        else:
          self.__displayMessage("")
          self.__game.board.flipCounters(row,column,self.__game.getplayer())
          self.__game.switchPlayer()
          self.__game.board.counterCount()     
      elif self.__game.reviewState() == "p":
        self.__displayMessage("The player has passed!")
        self.__updateGrid(window)
        if self.__game.checkWinner()[0] == True:
          self.__displayMessage(self.__game.checkWinner()[1])
          self.__freezeButtons()
      self.__game.board.getPossibleMoves(self.__game.getplayer(),self.__game.getOpposingPlayer())
      self.__updateGrid(window)


      if self.__game.reviewState() != "p":

        #Calculate a move using the Tree and Minimax algorithm

        aiEngine = AIEngine(self.__gamemode.split(" ")[0])
        aimove = aiEngine.getBestMove(self.__game.board)
        self.__game.play(int(aimove[0]),int(aimove[-1]))
        self.__game.board.flipCounters(int(aimove[0]),int(aimove[-1]),self.__game.getplayer())
        self.__game.switchPlayer()
        self.__game.board.counterCount()
        self.__updateGrid(window,aimove)

      if self.__game.reviewState() == "p":
        self.__displayMessage("The AI has passed!")
        self.__updateGrid(window)
        if self.__game.checkWinner()[0] == True:
          self.__displayMessage(self.__game.checkWinner()[1])
          self.__freezeButtons()

  def __undo(self,window):
    self.__game.undoMove()
    self.__updateGrid(window)  
    self.__passMessage.config(text="")    

  def __hint(self,window):
    findHint = AIEngine("hint")
    hintMove = findHint.getBestMove(self.__game.board)
    self.__updateGrid(window,None,hintMove)

  def __displayMessage(self,message):
    self.__passMessage.config(text=message,font=("Arial",18))
  
  def __freezeButtons(self):
    self.__undoButton.config(state=tk.DISABLED)
    self.__hintButton.config(state=tk.DISABLED)
  



    

    








    
    


        
