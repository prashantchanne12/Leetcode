class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        rows = len(board)
        cols = len(board[0])

        path = set()

        def dfs(row, col, i):

            if i == len(word):
                return True

            # out of bounds
            if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != word[i] or (row, col) in path:
                return False

            path.add((row, col))

            res = (dfs(row+1, col, i+1) or
                   dfs(row-1, col, i+1) or
                   dfs(row, col+1, i+1) or
                   dfs(row, col-1, i+1))

            path.remove((row, col))
            return res

        for r in range(rows):
            for c in range(cols):

                if dfs(r, c, 0):
                    return True

        return False

# O(n * m * 4^n)
