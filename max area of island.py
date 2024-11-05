'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0 
        visited = [[False for i in range(0, len(grid[0]))] for i in range(0, len(grid))]
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i == rows or j == cols or grid[i][j] == 0 or visited[i][j]:
                return 0

            visited[i][j] = True
            count = 1
            
            count += dfs(i + 1, j)
            count += dfs(i - 1, j)
            count += dfs(i, j + 1)
            count += dfs(i, j - 1)

            return count
        
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    count = dfs(i, j)
                    max_area = max(max_area, count)

        return max_area

            
