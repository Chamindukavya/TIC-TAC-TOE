"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = sum(row.count(X) for row in board)
    count_y = sum(row.count(O) for row in board)

    value = EMPTY
    if count_x > count_y:
        value = "O"
    else:
        value = "X"

    return value


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = []

    for i in range(3):
        for j in range(3):
            if(board[i][j] == EMPTY):
                possibleActions.append((i,j))

    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    xCount = 0
    ocount = 0

    for row in board:
        xCount = row.count('X')
        ocount = row.count('O')

        if xCount == 3:
            return X
        elif ocount == 3:
            return O

    xCount = 0
    ocount = 0
    for i in range(3):
        for j in range(3):
            if board[j][i] == X:
                xCount += 1
            elif board[j][i] == O:
                ocount += 1

            if xCount == 3:
                return X
            elif ocount == 3:
                return O
        xCount =0
        ocount=0    

    xCount = 0
    ocount = 0       

    diagonal1 = [board[0][0],board[1][1],board[2][2]] 
    diagonal2 = [board[0][2],board[1][1],board[2][0]] 
    
    xCount = diagonal1.count('X')
    ocount = diagonal1.count('O')

    if xCount == 3:
        return X
    elif ocount == 3:
        return O
    
    xCount = 0
    ocount = 0 

    xCount = diagonal2.count('X')
    ocount = diagonal2.count('O')

    if xCount == 3:
        return X
    elif ocount == 3:
        return O

    xCount = 0
    ocount= 0
    return

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    utilityVal = utility(board)
    emptyCount = sum(row.count(EMPTY) for row in board)

    if utilityVal == 1:
        return True
    elif utilityVal == -1:
        return True
    elif emptyCount == 0:
        return True
    else:
        False


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    utilityVal = utility(board)
    emptyCount = sum(row.count(EMPTY) for row in board)

    if utilityVal == 1:
        return True
    elif utilityVal == -1:
        return True
    elif emptyCount == 0:
        return True
    else:
        False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winnerOfMatch = winner(board)

    if winnerOfMatch == X:
        return 1
    
    elif winnerOfMatch == O:
        return -1
    
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
