from collections import deque


def bfs_matrix(arr):

    seen = [[False for x in range(len(arr[0]))] for y in range(len(arr))]

    values = []
    q = deque()

    q.append((0, 0))

    while q and len(values) != len(arr) * len(arr[0]):
        size = len(q)
        for i in range(size):

            row, col = q.popleft()

            if row >= len(arr) or row < 0 or col >= len(arr[0]) or col < 0:
                break

            if seen[row][col]:
                break

            values.append(arr[row][col])
            seen[row][col] = True

            q.append((row-1, col))
            q.append((row, col+1))
            q.append((row+1, col))
            q.append((row, col-1))

    return values


matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]


print(bfs_matrix(matrix))
