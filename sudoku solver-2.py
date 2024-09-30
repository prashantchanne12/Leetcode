'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:
'''

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(board, row, col, num):
            for i in range(0, 10):
                # check if the same column has that number
                if board[i][col] == num:
                    return False
                
                # check if the same row has that number
                if board[row][i] == num:
                    return False

                # check if the same 3x3 board ha that number
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                    return False

            return True

        def solve(board):
            for i in range(0, len(board)):
                for j in range(0, len(board[0])):
                    # 1) Look for the empty position
                    if board[i][j] == '.':
                        # 2) Let's try numbers 1-9 in this empty positions
                        for num in range(1, 10):
                            if is_valid(board, i, j, num):
                                board[i][j] = str(num)

                            if solve(board):
                                return True
                            else:
                                board[i][j] = '.'

                    return False

            return True
            


                            


