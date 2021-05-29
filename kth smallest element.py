'''
Given an unsorted array of numbers, find Kth smallest number in it.

Example 1:

Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].
Example 2:

Input: [1, 5, 12, 2, 11, 5], K = 4
Output: 5
Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].
Example 3:

Input: [5, 12, 11, -1, 12], K = 3
Output: 11
Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].
'''

from heapq import *


def kth_smallest_number(nums, k):

    max_heap = []

    for i in range(0, k):
        heappush(max_heap, -nums[i])

    print(max_heap)

    for i in range(k, len(nums)):

        if -nums[i] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])

        print(max_heap)

    return -max_heap[0]


print(kth_smallest_number([1, 2, 3, 4, 5, 6], 4))
print(kth_smallest_number([5, 12, 11, -1, 12], 3))
