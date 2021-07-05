'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
'''


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        if n <= 2:
            return nums.reverse()

        pointer = n-2

        # move the pointer until we find ending of desceding
        while pointer >= 0 and nums[pointer] >= nums[pointer+1]:
            pointer -= 1

        # last permutation of number
        # 3 2 1
        if pointer == -1:
            return nums.reverse()

        # 1 2 3
        # 1 3 2
        for i in range(n-1, pointer, -1):

            if nums[pointer] < nums[i]:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                break

        nums[pointer + 1:] = reversed(nums[pointer + 1:])

        return nums
