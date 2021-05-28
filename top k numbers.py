'''
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]
Example 2:

Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]
'''

from heapq import *


def find_k_largest_numbers(nums, k):

    min_heap = []

    # put first 'k' numbers in the min_heap
    for i in range(0, k):
        heappush(min_heap, nums[i])

    for i in range(k, len(nums)):

        # go through the remaining numbers of the array, if the number from the array is bigger than the,
        # top(smallest) number of the min-heap, remove the top from heap and add the number from the array
        if nums[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[i])

    return list(min_heap)


print(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3))
