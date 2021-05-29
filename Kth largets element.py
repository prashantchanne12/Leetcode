from heapq import *
'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
'''

# Solution - 1


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[::-1][k-1]

# Solution - 2 (preferred)


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        min_heap = []

        for i in range(0, k):
            heappush(min_heap, nums[i])

        for i in range(k, len(nums)):

            if nums[i] > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, nums[i])

        return min_heap[0]
