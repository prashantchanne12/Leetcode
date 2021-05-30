'''
Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

Example 1:

Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
Output: 23
Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
between 5 and 15 is 23 (11+12).
Example 2:

Input: [3, 5, 8, 7], and K1=1, K2=4
Output: 12
Explanation: The sum of the numbers between the 1st smallest number (3) and the 4th smallest 
number (8) is 12 (5+7).
'''

from heapq import *

# Solution 1


def find_sum_of_elements_1(nums, k1, k2):

    nums.sort()
    res = 0

    for i in range(k1, k2-1):
        res += nums[i]

    return res

# Solution - 2


def find_sum_of_elements_2(nums, k1, k2):

    min_heap = []
    res = 0
    final = k2-k1-1

    for num in nums:
        heappush(min_heap, num)

    while k1 != 0:
        heappop(min_heap)
        k1 -= 1

    while final != 0 and min_heap:
        res += heappop(min_heap)
        final -= 1

    return res
