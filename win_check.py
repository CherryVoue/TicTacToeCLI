#  Sets rows and columns to their own lists, determines if all symbols in a row/column are the same and not '#'. Checks for diagonal wins separately
def check(board):
    rows = [board[:3], board[3:6], board[6:]]
    columns = [[], [], []]

    for i in range(3):
        columns[i].append(board[i])
        columns[i].append(board[i+3])
        columns[i].append(board[i+6])

    for i in range(3):
        if all(x == rows[i][0] and x != '#' for x in rows[i]):
            return rows[i][0]
        if all(x == columns[i][0] and x != '#' for x in columns[i]):
            return columns[i][0]
            
    if board[4] != '#':
        if board[0] == board[4] and board[4] == board[8]:
            return board[4]
                
        if board[2] == board[4] and board[4] == board[6]:
            return board[4]
        
    return False
    
#  Only used in the gui version, returns how the game was won
def check_winner(board):
    rows = [board[:3], board[3:6], board[6:]]
    columns = [[], [], []]

    for i in range(3):
        columns[i].append(board[i])
        columns[i].append(board[i+3])
        columns[i].append(board[i+6])

    for i in range(3):
        if all(x == rows[i][0] and x != '#' for x in rows[i]):
            return rows[i][0], 'r', i
        if all(x == columns[i][0] and x != '#' for x in columns[i]):
            return columns[i][0], 'c', i
            
    if board[4] != '#':
        if board[0] == board[4] and board[4] == board[8]:
            return board[4], 'backslash', 0
                
        if board[2] == board[4] and board[4] == board[6]:
            return board[4], 'forwardslash', 0
        
    return False