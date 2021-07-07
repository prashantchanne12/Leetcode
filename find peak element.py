'''
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
'''


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        if left == right:
            return left

        while left <= right:

            # mirightd = left + (right - left) / 2
            mid = (left+right) // 2

            if mid > 0 and mid < len(nums) - 1:
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    return mid

                elif nums[mid-1] > nums[mid]:
                    right = mid - 1

                else:
                    left = mid + 1

            elif mid == 0:

                if nums[mid] > nums[mid+1]:
                    return 0
                else:
                    return 1

            elif mid == len(nums) - 1:

                if nums[len(nums)-1] > nums[len(nums)-2]:
                    return len(nums) - 1
                else:
                    return len(nums) - 2
