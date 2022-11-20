import tictactoe
from random import randint


#  Takes tictactoe Board class as argument to use for bot gameplay
class Bot:
    def __init__(self, play):
        self.play = play
        
    
    #  Move prio: Center, winning for bot, deny winning for player, side, random
    def bot_move(self):
        if self.play.board[4] == '#':
            return 4
        
        for i in range(len(self.play.board)):
            if self.play.board[i] == '#':
                self.play.board[i] = self.play.symbols[self.play.turn%2]
                if self.play.win_check(self.play.board):
                    self.play.board[i] = '#'
                    return i
                self.play.board[i] = '#'
        
        for i in range(len(self.play.board)):
            if self.play.board[i] == '#':
                self.play.board[i] = self.play.symbols[(self.play.turn+1)%2]
                if self.play.win_check(self.play.board):
                    self.play.board[i] = '#'
                    return i
                self.play.board[i] = '#'
                
        self.sides = [1, 3, 7, 5]
        self.corners = [0, 6, 8, 2]
        for i in range(4):
            if self.play.board[self.sides[i]] == self.play.symbols[(self.play.turn+1)%2]:
                if self.play.board[self.corners[i]] == '#':
                    return self.corners[i]
            if self.play.board[self.corners[i]] == self.play.symbols[(self.play.turn+1)%2]:
                if self.play.board[self.sides[i]] == '#':
                    return self.sides[i]
        
        return randint(0,8)
    

    #  See loop in main game, added differentiation for bot vs player turns
    def bot_loop(self):
        self.play.view_board()
    
        self.bot_turn = randint(0,1)
    
        while '#' in self.play.board:
            self.play.turn += 1
            
            if self.play.turn%2 == self.bot_turn:
                print(f'Player {self.play.symbols[self.play.turn%2]} (Bot) move location: ')
                while not self.play.play_move(self.bot_move()):
                    pass
                
            else:
                while not self.play.play_move(int(input(f'Player {self.play.symbols[self.play.turn%2]} (You) move location: '))):
                    print('Illegal move.')
                    
            if self.play.win_check(self.play.board):
                if self.play.turn%2 == self.bot_turn:
                    return f'Player {self.play.symbols[self.play.turn%2]} (Bot) wins!'
                else:
                    return 'game'# f'Player {self.play.symbols[self.play.turn%2]} (You) wins!'
                
        return "Draw"


#  Runtime control, passes main file's Board class into Bot class before starting the game
if __name__ == "__main__":
    game = Bot(tictactoe.Board())
    print(game.bot_loop())