import random


class Board:
    def __init__(self):
        self.board = ['#','#','#',
                      '#','#','#',
                      '#','#','#']
        self.turn = 0
        self.symbols = ['X','O']
        
    
    def view_board(self):
        print(f'{self.board[0]} {self.board[1]} {self.board[2]}',
              f'{self.board[3]} {self.board[4]} {self.board[5]}',
              f'{self.board[6]} {self.board[7]} {self.board[8]}\n',
              sep = '\n')
    
    
    def get_legal_moves(self):
        self.legals = []
        for i in range(len(self.board)):
            if self.board[i] == '#':
                self.legals.append(i)
        return self.legals
    
    
    def play_move(self, move):
        if not move in self.get_legal_moves():
            return False
        
        self.board[move] = self.symbols[self.turn%2]
        self.view_board()
        return True
    
    
    def win_check(self):
        self.checks = [0,3,6]
        
        for i in range(3):
            if self.board[self.checks[i]+1] != '#' and self.board[self.checks[i]] == self.board[self.checks[i]+1] and self.board[self.checks[i]+1] == self.board[self.checks[i]+2]:
                return True
            
            if self.board[i] != '#' and self.board[i+3] == self.board[i] and self.board[i] == self.board[i+6]:
                return True
        
            if self.board[4] != '#':
                if self.board[0] == self.board[4] and self.board[4] == self.board[8]:
                    return True
                
                if self.board[2] == self.board[4] and self.board[4] == self.board[6]:
                    return True
        return False
    
    
    def gameplay_loop(self):
        while self.get_legal_moves() != []:
            self.turn += 1
            while not self.play_move(int(input(f'Player {self.symbols[self.turn%2]} move location: '))):
                print('Illegal move.')
            if self.win_check():
                return f'{self.symbols[self.turn%2]} wins!'
        return "Draw"
                
        
if __name__ == "__main__":
    play = Board()
    print(play.gameplay_loop())
    
    
    
    
    
    
    
    
    
    
    
