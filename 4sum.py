'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [], target = 0
Output: []
'''


def search_pair(nums, target, i, j, q):
    left = j+1
    right = len(nums) - 1

    while left < right:

        current_sum = nums[i] + nums[j] + nums[left] + nums[right]

        if current_sum == target:
            q.append([nums[i], nums[j], nums[left], nums[right]])

            left += 1
            right -= 1

            while left < right and nums[left] == nums[left-1]:
                left += 1

            while left < right and nums[right] == nums[right+1]:
                right -= 1

        elif current_sum < target:
            left += 1
        else:
            right -= 1


def four_sum(nums, target):
    nums.sort()
    q = []

    for i in range(0, len(nums)-3):

        if i > 0 and nums[i] == nums[i-1]:
            continue

        for j in range(i+1, len(nums)-2):

            if j > i+1 and nums[j] == nums[j-1]:
                continue

            search_pair(nums, target, i, j, q)

    return q


nums = [2, 0, -1, 1, -2, 2]
target = 2
print(four_sum(nums, target))
