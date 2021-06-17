'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        row_zero = False

        # determing which rows or cols need to be 0
        for row in range(rows):
            for col in range(cols):

                if matrix[row][col] == 0:

                    matrix[0][col] = 0

                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        row_zero = True

        for row in range(1, rows):
            for col in range(1, cols):

                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for row in range(rows):
                matrix[row][0] = 0

        if row_zero:
            for col in range(cols):
                matrix[0][col] = 0
