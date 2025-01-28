'''
'''

# Solution 1
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == 1:
                    # check top
                    if row-1 < 0 or grid[row-1][col] == 0:
                        perimeter += 1

                    # check right
                    if col + 1 >= len(grid[0]) or grid[row][col + 1] == 0:
                        perimeter += 1

                    # check bottom
                    if row + 1 >= len(grid) or grid[row+1][col] == 0:
                        perimeter += 1

                    # check right:
                    if col - 1 < 0 or grid[row][col-1] == 0:
                        perimeter += 1

        return perimeter        
        
# Solution 2
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        visited = set()

        def dfs(row, col):
            if (row, col) in visited:
                return 0

            if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] == 0:
                return 1

            visited.add((row, col))

            top = dfs(row - 1, col)
            right = dfs(row, col + 1)
            bottom = dfs(row + 1, col)
            left = dfs(row, col - 1)
            

            return top + right + bottom + left

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == 1:
                    perimeter += dfs(row, col)

        return perimeter        
        
        