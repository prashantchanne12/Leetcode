'''
rows columns

[-1, 0] up
[ 0, 1] right
[ 1, 0] down
[ 0,-1] left

'''


def dfs_matrix(arr):

    seen = [[False for i in range(len(arr))] for i in range(len(arr[0]))]

    values = []

    dfs_recusrive(arr, 0, 0, seen, values)

    return values


def dfs_recusrive(arr, row, col, seen, values):

    if len(values) == len(arr) * len(arr[0]):
        return

    if row >= len(arr) or row < 0:
        return

    if col >= len(arr[0]) or col < 0:
        return

    if seen[row][col]:
        return

    values.append(arr[row][col])
    seen[row][col] = True

    dfs_recusrive(arr, row-1, col, seen, values)
    dfs_recusrive(arr, row, col+1, seen, values)
    dfs_recusrive(arr, row+1, col, seen, values)
    dfs_recusrive(arr, row, col-1, seen, values)


arr = [[0, 1, 2, 3],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]

print(dfs_matrix(arr))
