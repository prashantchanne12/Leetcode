'''
The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other. For example, following is a solution for 4 Queen problem.

The expected output is a binary matrix which has 1s for the blocks where queens are placed. For example, following is the output matrix for above 4 queen solution.

{ 0,  1,  0,  0}
{ 0,  0,  0,  1}
{ 1,  0,  0,  0}
{ 0,  0,  1,  0}
'''


def is_safe(board, row, col, n):

    # Checking rows -->
    for i in range(0, col):
        if board[row][i] == 1:
            return False

    # Checking columns
    for i in range(0, row):
        if board[i][col] == 1:
            return False

    # Checking up-left diagonally
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    # Checking up-right diagonally
    i = row
    j = col

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False

        i -= 1
        j += 1

    return True


def n_queen(board, row, n):

    if row == n:
        return True

    for col in range(0, n):

        if is_safe(board, row, col, n):

            board[row][col] = 1

            if (n_queen(board, row+1, n)):
                return True

            board[row][col] = 0

    return False


n = 4
board = [[0 for x in range(n)] for y in range(n)]

print(n_queen(board, 0, n))

for row in board:
    print(row)
