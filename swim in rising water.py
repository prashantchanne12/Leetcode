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