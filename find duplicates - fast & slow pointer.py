'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [1,1]
Output: 1
Example 4:

Input: nums = [1,1,2]
Output: 1
'''


def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    pointer_1 = nums[0]
    pointer_2 = slow

    while pointer_1 != pointer_2:
        pointer_1 = nums[pointer_1]
        pointer_2 = nums[pointer_2]

    return pointer_1


print(find_duplicate([3, 1, 3, 4, 2]))
