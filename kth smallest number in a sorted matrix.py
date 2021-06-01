'''
Given an N * NN∗N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.

Example 1:

Input: Matrix=[
    [2, 6, 8], 
    [3, 7, 10],
    [5, 8, 11]
  ], 
  K=5
Output: 7
Explanation: The 5th smallest number in the matrix is 7.
'''

from heapq import *


def find_kth_largest(matrix, k):

    min_heap = []

    for i in range(0, len(matrix)):

        heappush(min_heap, (matrix[i][0], 0, matrix[i]))

    number_count = 0

    while min_heap:

        num, index, row = heappop(min_heap)

        number_count += 1

        if number_count == k:
            break

        if len(matrix) > index+1:
            heappush(min_heap, (row[index+1], index+1, row))

    return num


print(find_kth_largest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5))
