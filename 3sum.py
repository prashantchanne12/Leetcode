'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
'''


def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1

            while left < right and arr[left] == arr[left-1]:
                left += 1

            while left < right and arr[right] == arr[right+1]:
                right -= 1

        elif target_sum > current_sum:
            left += 1

        else:
            right -= 1


class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        triplets = []

        for i in range(0, len(nums)):

            if i > 0 and nums[i] == nums[i-1]:  # skip duplicate
                continue

            search_pair(nums, -nums[i], i+1, triplets)

        return triplets
