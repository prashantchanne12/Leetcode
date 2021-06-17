'''
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
'''


class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        new_matrix = [[0 for x in range(len(matrix))]
                      for y in range(len(matrix[0]))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):

                new_matrix[col][row] = matrix[row][col]

        return new_matrix


'''
 [1, 2, 3],
 [4, 5, 6]

 [1, 4],
 [2, 5],
 [3, 6]
 
 '''
