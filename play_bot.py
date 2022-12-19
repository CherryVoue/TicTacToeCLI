"""
Heavy influence from these three sites:
https://github.com/Cledersonbc/tic-tac-toe-minimax
https://levelup.gitconnected.com/mastering-tic-tac-toe-with-minimax-algorithm-3394d65fa88f
https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/
"""
from win_check import check
import math

#  Takes tictactoe Board and turn number as arguments
class Bot:
    def __init__(self, board, turn):
        self.board = board
        self.turn = turn
        self.symbols = ['X','O']
     
     
    def empty(self):
    #  Returns the indexes of all available positions
        slots = []
        for i in range(len(self.board)):
            if self.board[i] == '#':
                slots.append(i)
        return slots
    
    
    def move(self):
    #  Returns the move value from the minimax function's list ([best move, score])
        return self.minimax(self.board.count('#'), self.turn)[0]
    
    
    def minimax(self, depth, turn):
    #  Uses depth directly related to amount of open spaces and turn count to determine optimal moves
        if turn%2 == 1:
           best = [None, -math.inf]
        else:
            best = [None, math.inf]
            
        if (end := check(self.board)) != False or depth == 0:
            if end != False:
                return [None, 1] if end == 'O' else [None, -1]
            return [None, 0]
            
        for slot in self.empty():
            self.board[slot] = self.symbols[turn%2]
            score = self.minimax(depth-1, turn+1)
            self.board[slot] = '#'
                
            score[0] = slot
            
            if turn%2 == 1:
                if score[1] > best[1]:
                    best = score
            else:
                if score[1] < best[1]:
                    best = score
                
        return best