#  Initialize playing board, turn count, and game symbols
class Board:
    def __init__(self):
        self.board = ['#','#','#',
                      '#','#','#',
                      '#','#','#']
        self.turn = 0
        self.symbols = ['X','O']
        

    #  Prints board in easy-to-read manner
    def view_board(self):
        print(f'{self.board[0]} {self.board[1]} {self.board[2]}',
              f'{self.board[3]} {self.board[4]} {self.board[5]}',
              f'{self.board[6]} {self.board[7]} {self.board[8]}\n',
              sep = '\n')
    
    #  True/False depending on whether the move is valid/invalid, valid move is placed on the board, triggers view_board
    def play_move(self, move):
        if move > 8 or not self.board[move] == '#':
            return False
        
        self.board[move] = self.symbols[self.turn%2]
        self.view_board()
        return True
    
    #  Sets rows and columns to their own lists, determines if all symbols in a row/column are the same and not '#'. Checks for diagonal wins separately
    def win_check(self):
        self.rows = [self.board[:3], self.board[3:6], self.board[6:]]
        self.columns = [[], [], []]

        for i in range(3):
            self.columns[i].append(self.board[i])
            self.columns[i].append(self.board[i+3])
            self.columns[i].append(self.board[i+6])

        for i in range(3):
            if all(x == self.rows[i][0] and x != '#' for x in self.rows[i]):
                return True
            if all(x == self.columns[i][0] and x != '#' for x in self.columns[i]):
                return True
            
        if self.board[4] != '#':
            if self.board[0] == self.board[4] and self.board[4] == self.board[8]:
                return True
                
            if self.board[2] == self.board[4] and self.board[4] == self.board[6]:
                return True
            
        return False
    
    #  Starts off printing the board, while loop continues until board is full (and determines draw) or a player wins. Embedded loop continues until a valid move is played
    def gameplay_loop(self):
        self.view_board()
        while '#' in self.board:
            self.turn += 1
            while not self.play_move(int(input(f'Player {self.symbols[self.turn%2]} move location: '))):
                print('Illegal move.')
            if self.win_check():
                return f'{self.symbols[self.turn%2]} wins!'
        return "Draw"

#  Runtime control, lines will not run if this file is imported elsewhere
if __name__ == "__main__":
    play = Board()
    print(play.gameplay_loop())
