'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
'''

from collections import deque


def rotten_oranges(matrix):

    if len(matrix) == 0:
        return 0

    fresh_count = 0
    q = deque()

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):

            if matrix[row][col] == 2:
                q.append((row, col))

            if matrix[row][col] == 1:
                fresh_count += 1

    fresh_count, minutes = bfs(matrix, q, fresh_count)

    if fresh_count > 0:
        return -1

    return minutes-1


def bfs(matrix, q, fresh_count):

    minutes = 0
    current_q_size = len(q)

    while q:

        if current_q_size == 0:
            minutes += 1
            current_q_size = len(q)

        for i in range(len(q)):

            row, col = q.popleft()
            current_q_size -= 1

            if row >= len(matrix) or row < 0 or col >= len(matrix[0]) or col < 0:
                break

            if matrix[row][col] == 0:
                break

            matrix[row][col] = 0
            fresh_count -= 1

            q.append((row, col+1))
            q.append((row+1, col))
            q.append((row, col-1))
            q.append((row-1, col))

    return fresh_count, minutes


matrix_1 = [
    [2, 1, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1]
]

matrix_2 = [
    [2, 0, 1, 0, 0],
    [1, 1, 0, 0, 2],
    [0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1]
]

print(rotten_oranges(matrix_1))
