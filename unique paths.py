'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

 

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2

Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6
'''


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[1 if i == m-1 or j == n-1 else -
               1 for i in range(m)] for j in range(n)]

        return self.matrix_paths_recursive(0, 0, n-1, m-1, dp)

    def matrix_paths_recursive(self, i, j, n, m, dp):

        if dp[i][j] != -1:
            return dp[i][j]

        dp[i][j] = self.matrix_paths_recursive(
            i+1, j, n, m, dp) + self.matrix_paths_recursive(i, j+1, n, m, dp)

        return dp[i][j]
