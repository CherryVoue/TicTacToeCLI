#  Import tkinter (gui), tkinter ttk (updates visuals), tictactoe cli game, win_check module,
#  play_bot module, random for determining who goes first
from tkinter import *
from tkinter.ttk import *
from tictactoe import Board
from win_check import check, check_winner
from play_bot import Bot
from random import randint


class Game(Tk):
    def __init__(self):
        #  Tkinter child class
        super().__init__()
        
        #  Get width and height of screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        #  Set default window size
        win_x = screen_width
        win_y = screen_height
        
        #  Set default text font and size for all buttons
        style = Style(self)
        style.configure('TButton', font=('TkDefaultFont', 50))
        
        #  Set visual for winner's slots
        style.configure('winner.TButton', font=('TkDefaultFont', 50), foreground='green')

        #  Find center of screen
        center_x = int(screen_width/2 - win_x / 2)
        center_y = int(screen_height/2 - win_y / 2)
        
        #  Set title and size of window
        self.title('TicTacToe')
        self.geometry(f'{win_x}x{win_y}+{center_x}+{center_y}')
        
        #  Window is not resizeable
        self.resizable(False, False)
        
        #  Columns 0, 1, 2 all same size (width)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        
        #  Row 0 has no weight - smaller, rows 1, 2, 3 have the same size (height)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        
        #  Get board state and replace all '#'s with ' ' for display purposes
        self.state = list(map(lambda x: x.replace('#', ' '), play.get_board()))
        
        #  Set label for default winner state
        self.lbl_game_state = Label(self, text='Winner: ')
        
        if play.bot_game:
            #  Set label for default bot time if playing against bot
            self.lbl_time = Label(self, text='Bot Evaluation time: 0')
        
        #  Starts the game loop
        self.gui_gameplay_loop()
        
    
    def build_board(self):
        #  Displays bot evaulutaion time in grid if playing against bot
        if play.bot_game:
            self.lbl_time.grid(column=2, row=0, sticky = 'w')
        
        #  Places turn, winner labels, slot buttons in grid
        self.lbl_turn.grid(column=0, row=0, sticky = 'w')
        self.lbl_game_state.grid(column=1, row=0, sticky = 'w')
        
        self.slot0.grid(column=0, row=1, sticky = 'news')
        self.slot1.grid(column=1, row=1, sticky = 'news')
        self.slot2.grid(column=2, row=1, sticky = 'news')
        
        self.slot3.grid(column=0, row=2, sticky = 'news')
        self.slot4.grid(column=1, row=2, sticky = 'news')
        self.slot5.grid(column=2, row=2, sticky = 'news')
        
        self.slot6.grid(column=0, row=3, sticky = 'news')
        self.slot7.grid(column=1, row=3, sticky = 'news')
        self.slot8.grid(column=2, row=3, sticky = 'news')
        
    def gui_gameplay_loop(self):
        #  Sets label for player turn
        self.lbl_turn = Label(self, text=f'Turn: {play.get_symbol()}')
        
        #  Sets button values for each board position, on click triggers self.btn_move() function for that slot
        self.slot0 = Button(self, text=self.state[0], command = lambda: self.btn_move(0))
        self.slot1 = Button(self, text=self.state[1], command = lambda: self.btn_move(1))
        self.slot2 = Button(self, text=self.state[2], command = lambda: self.btn_move(2))
        
        self.slot3 = Button(self, text=self.state[3], command = lambda: self.btn_move(3))
        self.slot4 = Button(self, text=self.state[4], command = lambda: self.btn_move(4))
        self.slot5 = Button(self, text=self.state[5], command = lambda: self.btn_move(5))
        
        self.slot6 = Button(self, text=self.state[6], command = lambda: self.btn_move(6))
        self.slot7 = Button(self, text=self.state[7], command = lambda: self.btn_move(7))
        self.slot8 = Button(self, text=self.state[8], command = lambda: self.btn_move(8))
        
        
        #  Condition for the bot to play, see self.bot_move()
        if play.bot_game and play.turn%2 == 1:
            self.bot_move()
        
        #  Conditions for changing the winner label, previous labels are destroyed to prevent text stacking
        if (winner := check(play.get_board())) != False:
            #  Checks for winner
            self.lbl_game_state.destroy()
            self.lbl_game_state = Label(self, text=f'Winner: {winner}')
            self.win_visual()
        if not ' ' in self.state:
            #  Checks for draw
            self.lbl_game_state.destroy()
            self.lbl_game_state = Label(self, text='Winner: Draw')
        
        #  Builds board visual
        self.build_board()
    
    
    def btn_move(self, move):
        #  Resets game if the game is over before button is pressed
        if self.state.count(' ') == 0 or check(play.get_board()) != False:
            play.board = ['#','#','#','#','#','#','#','#','#']
            self.lbl_game_state.destroy()
            self.lbl_game_state = Label(self, text='Winner: ')
            play.turn = randint(0,1)
        
        #  Player move if turn%2 = 0 or if two humans are playing, increases turn counter
        else:
            #  Print move in console, if move is valid, play it
            if play.bot_game == 0 or play.turn%2 == 0:
                print(move)
                if play.play_move(move) != False:
                    play.turn += 1
        
        #  Get board state and replace all '#'s with ' ' for display purposes
        self.state = list(map(lambda x: x.replace('#', ' '), play.get_board()))
        
        #  Back to gameplay loop
        self.gui_gameplay_loop()
        
        
    def bot_move(self):
        #  Increases turn count if no moves are available (human played in last available slot
        if self.state.count(' ') == 0 or check(play.get_board()) != False:
            play.turn += 1
        
        #  Bot plays if slot(s) available
        else:
            #  Initializes Bot class from play_bot.py
            bot = Bot(play.get_board(), play.turn)
            #  Calls the bot to make its move determined via minimax algorithm
            move, time = bot.move()
            
            #  Label for bot evaluation time destroyed and replaced with new value (destroyed to prevent text stacking)
            self.lbl_time.destroy()
            self.lbl_time = Label(self, text=f'Bot Evaluation time: {round(time, 7)}s')
            
            #  Prints the bot's move in the console
            print(move)
            
            #  Playes the bot's move and increases turn counter
            play.play_move(move)
            play.turn += 1
            
            #  Get board state and replace all '#'s with ' ' for display purposes
            self.state = list(map(lambda x: x.replace('#', ' '), play.get_board()))
        
        #  Back to gameplay loop
        self.gui_gameplay_loop()
        
        
    def win_visual(self):
        #  Sets winning lane to green
        sym, lane, num = check_winner(play.get_board())
        if lane == 'r':
            if num == 0:
                self.slot0 = Button(self, text=self.state[0], style='winner.TButton', command = lambda: self.btn_move(0))
                self.slot1 = Button(self, text=self.state[1], style='winner.TButton', command = lambda: self.btn_move(1))
                self.slot2 = Button(self, text=self.state[2], style='winner.TButton', command = lambda: self.btn_move(2))
            elif num == 1:
                self.slot3 = Button(self, text=self.state[3], style='winner.TButton', command = lambda: self.btn_move(3))
                self.slot4 = Button(self, text=self.state[4], style='winner.TButton', command = lambda: self.btn_move(4))
                self.slot5 = Button(self, text=self.state[5], style='winner.TButton', command = lambda: self.btn_move(5))
            elif num == 2:
                self.slot6 = Button(self, text=self.state[6], style='winner.TButton', command = lambda: self.btn_move(6))
                self.slot7 = Button(self, text=self.state[7], style='winner.TButton', command = lambda: self.btn_move(7))
                self.slot8 = Button(self, text=self.state[8], style='winner.TButton', command = lambda: self.btn_move(8))
                
        elif lane == 'c':
            if num == 0:
                self.slot0 = Button(self, text=self.state[0], style='winner.TButton', command = lambda: self.btn_move(0))
                self.slot3 = Button(self, text=self.state[3], style='winner.TButton', command = lambda: self.btn_move(3))
                self.slot6 = Button(self, text=self.state[6], style='winner.TButton', command = lambda: self.btn_move(6))
            elif num == 1:
                self.slot1 = Button(self, text=self.state[1], style='winner.TButton', command = lambda: self.btn_move(1))
                self.slot4 = Button(self, text=self.state[4], style='winner.TButton', command = lambda: self.btn_move(4))
                self.slot7 = Button(self, text=self.state[7], style='winner.TButton', command = lambda: self.btn_move(7))
            elif num == 2:
                self.slot2 = Button(self, text=self.state[2], style='winner.TButton', command = lambda: self.btn_move(2))
                self.slot5 = Button(self, text=self.state[5], style='winner.TButton', command = lambda: self.btn_move(5))
                self.slot8 = Button(self, text=self.state[8], style='winner.TButton', command = lambda: self.btn_move(8))
                
        elif lane == 'backslash':
            self.slot0 = Button(self, text=self.state[0], style='winner.TButton', command = lambda: self.btn_move(0))
            self.slot4 = Button(self, text=self.state[4], style='winner.TButton', command = lambda: self.btn_move(4))
            self.slot8 = Button(self, text=self.state[8], style='winner.TButton', command = lambda: self.btn_move(8))
        elif lane == 'forwardslash':
            self.slot2 = Button(self, text=self.state[2], style='winner.TButton', command = lambda: self.btn_move(2))
            self.slot4 = Button(self, text=self.state[4], style='winner.TButton', command = lambda: self.btn_move(4))
            self.slot6 = Button(self, text=self.state[6], style='winner.TButton', command = lambda: self.btn_move(6))
                
        self.build_board()


#  Runtime control
if __name__ == "__main__":
    #  Asks the user whether they want to play the bot
    while (bot_game := input("Would you like to play against the bot? (1 for yes, 0 for no): ")) not in ['0','1']:
        print('Please select a valid option.')
        
    #  Initializes original game and starts the gui
    play = Board(bot_game)
    game = Game()
    game.mainloop()
