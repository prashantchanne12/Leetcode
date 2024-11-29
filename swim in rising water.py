'''
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

 

Example 1:


Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:


Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
 
'''
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        min_heap = [[grid[0][0], 0, 0]] # (height, row, col)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        visited.add((0, 0))

        while min_heap:
            max_height, row, col = heapq.heappop(min_heap)

            if row == n - 1 and col == n - 1:
                return max_height

            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc 

                if new_row < 0 or new_col < 0 or new_row == n or new_col == n or (new_row, new_col) in visited:
                    continue

                visited.add((new_row, new_col))
                heapq.heappush(min_heap, [max(max_height, grid[new_row][new_col]), new_row, new_col])