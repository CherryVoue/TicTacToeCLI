from tkinter import *
from tkinter.ttk import *
from tictactoe import Board
from win_check import check
from play_bot import Bot
from random import randint


class Game(Tk):
    def __init__(self):
        super().__init__()
        
        win_x = 550
        win_y = 600
        
        style = Style(self)
        style.configure('TButton', font=('TkDefaultFont', 50))

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - win_x / 2)
        center_y = int(screen_height/2 - win_y / 2)

        self.title('TicTacToe')
        self.geometry(f'{win_x}x{win_y}+{center_x}+{center_y}')

        self.resizable(False, False)
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        
        self.state = list(map(lambda x: x.replace('#', ' '), play.get_board()))
        
        self.lbl_game_state = Label(self, text='Winner: ')
        
        if play.bot_game:
            self.lbl_time = Label(self, text='Bot Evaluation time: 0')
        
        self.gui_gameplay_loop()
        
    
    def build_board(self):
        if play.bot_game:
            self.lbl_time.grid(column=2, row=0, sticky = 'w')
            
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
        self.lbl_turn = Label(self, text=f'Turn: {play.get_symbol()}')
        
        self.slot0 = Button(self, text=self.state[0], command = lambda: self.btn_move(0))
        self.slot1 = Button(self, text=self.state[1], command = lambda: self.btn_move(1))
        self.slot2 = Button(self, text=self.state[2], command = lambda: self.btn_move(2))
        
        self.slot3 = Button(self, text=self.state[3], command = lambda: self.btn_move(3))
        self.slot4 = Button(self, text=self.state[4], command = lambda: self.btn_move(4))
        self.slot5 = Button(self, text=self.state[5], command = lambda: self.btn_move(5))
        
        self.slot6 = Button(self, text=self.state[6], command = lambda: self.btn_move(6))
        self.slot7 = Button(self, text=self.state[7], command = lambda: self.btn_move(7))
        self.slot8 = Button(self, text=self.state[8], command = lambda: self.btn_move(8))
        
        
        
        if play.bot_game and play.turn%2 == 1:
            self.bot_move()
        
        if (winner := check(self.state)) != False:
            self.lbl_game_state.destroy()
            self.lbl_game_state = Label(self, text=f'Winner: {winner}')
        if not ' ' in self.state:
            self.lbl_game_state.destroy()
            self.lbl_game_state = Label(self, text='Winner: Draw')
        
        self.build_board()
    
    def btn_move(self, move):
        if self.state.count(' ') == 0 or check(play.get_board()) != False:
            play.board = ['#','#','#','#','#','#','#','#','#']
            self.lbl_game_state.destroy()
            self.lbl_game_state = Label(self, text='Winner: N/A')
            play.turn = randint(0,1)
            
        else:
            if play.bot_game == 0 or play.turn%2 == 0:
                print(move)
                if play.play_move(move) != False:
                    play.turn += 1
        
        self.state = list(map(lambda x: x.replace('#', ' '), play.get_board()))
        
        
        self.gui_gameplay_loop()
        
        
    def bot_move(self):
        if self.state.count(' ') == 0 or check(play.get_board()) != False:
            play.turn += 1
        
        else:
            bot = Bot(play.get_board(), play.turn)
            move, time = bot.move()
            
            self.lbl_time.destroy()
            self.lbl_time = Label(self, text=f'Bot Evaluation time: {round(time, 7)}s')
            
            print(move)
            
            play.play_move(move)
            play.turn += 1
            
            self.state = list(map(lambda x: x.replace('#', ' '), play.get_board()))
        
        self.gui_gameplay_loop()
        
#game.iconbitmap('icon.ico')
'''
exit_btn = Button(
    game,
    text='Exit',
    command = lambda: game.quit())
    
exit_btn2 = Button(
    game,
    text='Exit',
    command = lambda: game.quit())
    
exit_btn.pack(
    ipadx=5,
    ipady=5)
    
exit_btn2.pack()
'''
'''
Label(text='test').pack()

frm0 = Frame(master=game, width=50, height=50, bg="red")
frm0.pack(fill=BOTH, side=LEFT, expand=True)

frm1 = Frame(master=game, width=500, bg="yellow")
frm1.pack(fill=BOTH, side=LEFT, expand=True)

frm2 = Frame(master=game, width=50, bg="blue")
frm2.pack(fill=BOTH, side=LEFT, expand=True)
'''



if __name__ == "__main__":
    while (bot_game := input("Would you like to play against the bot? (1 for yes, 0 for no): ")) not in ['0','1']:
        print('Please select a valid option.')
        
    play = Board(bot_game)
    game = Game()
    game.mainloop()