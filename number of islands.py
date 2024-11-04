'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
from collections import deque


class Solution(object):
    def numIslands(self, grid):

        count = 0
        matrix = grid

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):

                if matrix[row][col] == '1':

                    count += 1
                    self.dfs(matrix, row, col)

        return count

    def dfs(self, matrix, row, col):

        q = deque()

        q.append((row, col))

        while q:
            size = len(q)

            for i in range(size):

                row, col = q.popleft()

                if row >= len(matrix) or row < 0 or col >= len(matrix[0]) or col < 0:
                    break

                if matrix[row][col] == '0':
                    break

                matrix[row][col] = '0'

                q.append((row, col+1))
                q.append((row+1, col))
                q.append((row, col-1))
                q.append((row-1, col))


# Solution 2 - DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i == rows or j == cols or grid[i][j] == "0" or visited[i][j]:
                return

            visited[i][j] = True

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    count += 1

        return count