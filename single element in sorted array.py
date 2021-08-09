'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
'''


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        # boundry check
        if right == 0:
            # only one element in the array
            return nums[0]

        elif nums[0] != nums[1]:
            return nums[0]

        elif nums[right] != nums[right-1]:
            return nums[right]

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            if (mid % 2) == 0 and nums[mid] == nums[mid+1] or (mid % 2) == 1 and nums[mid] == nums[mid-1]:
                left = mid + 1
            else:
                right = mid - 1

        return -1
