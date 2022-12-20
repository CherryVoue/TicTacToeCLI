from random import randint
from play_bot import Bot
from win_check import check


#  Initialize playing board, turn count, and game symbols
class Board:
    def __init__(self, bot_game):
        self.bot_game = int(bot_game)
        self.board = ['#','#','#',
                      '#','#','#',
                      '#','#','#']
        self.turn = randint(0,1)
        self.symbols = ['X','O']
        

    #  Prints board in easy-to-read manner
    def view_board(self):
        print(f'{self.board[0]} {self.board[1]} {self.board[2]}',
              f'{self.board[3]} {self.board[4]} {self.board[5]}',
              f'{self.board[6]} {self.board[7]} {self.board[8]}\n',
              sep = '\n')
    
    
    #  True/False depending on whether the move is valid/invalid, valid move is placed on the board, triggers view_board
    def play_move(self, move):
        if move > 8 or not self.board[move] == '#' or move < 0:
            return False
        
        self.board[move] = self.symbols[self.turn%2]
        self.view_board()
        return True
    
    
    #  Starts off printing the board, while loop continues until board is full (and determines draw) or a player wins. Embedded loop continues until a valid move is played
    def cli_gameplay_loop(self):
        self.view_board()
        while '#' in self.board:
            self.turn += 1
            if self.bot_game and self.turn%2 == 1:
                bot = Bot(self.board, self.turn)
                
                move, time = bot.move()
                
                print(f'Bot move location: {move}')
                print(f'Evaluation time {round(time, 7)}')
                
                self.play_move(move)
            
            else:
                while not self.play_move(int(input(f'Player {self.symbols[self.turn%2]} move location: '))):
                    print('Illegal move.')
            
            if check(self.board) != False:
                return f'{self.symbols[self.turn%2]} wins!'
        
        return "Draw"
        
    
    #  The below function(s) are only used in the gui version of the game
    def get_symbol(self):
        return self.symbols[self.turn%2]
        
    def get_board(self):
        return self.board

#  Runtime control, lines will not run if this file is imported elsewhere
if __name__ == "__main__":
    while (bot_game := input("Would you like to play against the bot? (1 for yes, 0 for no): ")) not in ['0','1']:
        print('Please select a valid option.')
        
    play = Board(bot_game)
    print(play.cli_gameplay_loop())
