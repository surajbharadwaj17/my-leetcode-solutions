"""
Wrte a function that prints a chessboard pattern, with W being white square 
and B being black.
Input: Integer that is the number of squares on the board
Output: N-d char array that represent the chess board pattern
"""

def createChessBoard(n):
    board = [['']*(n) for _ in range(n)]

    for i in range(n):

        if i % 2 == 0:
            board[i][0] = 'W'
        else:
            board[i][0] = 'B'
        
        prev = board[i][0]

        for j in range(1,n):
            if prev == 'B':
                board[i][j] = 'W'
                prev = 'W'
            else:
                board[i][j] = 'B'
                prev = 'B'

    return board

createChessBoard(2)