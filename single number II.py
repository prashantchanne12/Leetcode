'''
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99

'''

# Solution 1 - Dictionary


def single_number_1(nums):
    dict = {}

    for num in nums:
        if num not in dict:
            dict[num] = 0

        dict[num] += 1

    for key, val in dict.items():
        if val == 1:
            return key


print(single_number_1([2, 2, 3, 2]))

# Solution 2 - Bit manupalation


def single_number_2(nums):
    ones = 0
    twos = 0

    for num in nums:
        ones = (ones ^ num) & ~(twos)
        twos = (twos ^ num) & ~(ones)

    return ones


print(single_number_2([2, 2, 3, 2]))

# Solution 3 - Sorting (preffered + intuitive)


def single_number_3(nums):

    n = len(nums)

    if n < 3:
        return nums[0]

    nums.sort()

    # if number is at first index
    if nums[0] != nums[1]:
        return nums[0]

    i = 1

    while i < n:
        if nums[i] != nums[i-1]:
            return nums[i-1]

        i += 3

    # if number is at last index
    return nums[n-1]


print(single_number_3([2, 2, 3, 2]))
