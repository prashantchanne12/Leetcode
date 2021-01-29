'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):

        if n == 0:
            return nums1

        right = len(nums1) - 1

        for i in range(0, len(nums2)):
            nums1[right] = nums2[i]
            right -= 1

        nums1.sort()

        return nums1
