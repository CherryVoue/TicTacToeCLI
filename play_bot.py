"""
Heavy influence from:
https://github.com/Cledersonbc/tic-tac-toe-minimax
https://levelup.gitconnected.com/mastering-tic-tac-toe-with-minimax-algorithm-3394d65fa88f
https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/
"""
from win_check import check
import math
import time


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
        #  Returns the move value from the minimax function's list ([best move, score]) and evaluation time
        start = time.time()
        move = self.minimax(self.board.count('#'), self.turn)[0]
        end = time.time()
        return move, (end-start)
    
    
    def minimax(self, depth, turn):
        #  Uses depth directly related to amount of open spaces and turn count to determine optimal moves
        
        # Default move score [move, score]
        if turn%2 == 1:
            best = [None, -math.inf]
        else:
            best = [None, math.inf]
        
        #  Checks for end of game: score of 1 for bot win, -1 for human win, 0 for draw
        if (end := check(self.board)) != False or depth == 0:
            if end != False:
                return [None, 1] if end == 'O' else [None, -1]
            return [None, 0]
            
        #  Retrieves positions of all legal moves, makes a move and recursively fills out the board
        #  waiting for a terminal game state
        for slot in self.empty():
            #  Plays legal move
            self.board[slot] = self.symbols[turn%2]
            #  Function calls itself, filling out the board until win or draw
            score = self.minimax(depth-1, turn+1)
            #  Undo move
            self.board[slot] = '#'
                
            #  Place move into list with that move's score
            score[0] = slot
            
            #  Best move for maximizer (bot) is highest score possible
            if turn%2 == 1:
                if score[1] > best[1]:
                    best = score
            #  Best move for minimizer (human) is lowest score possible
            else:
                if score[1] < best[1]:
                    best = score
                
        #  Returns optimal [move, score] list
        return best