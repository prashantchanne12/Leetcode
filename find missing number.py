'''
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

Example 1:

Input: [4, 0, 3, 1]
Output: 2

Example 2:

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
'''

def find_missing_number(nums):
    n = len(nums)
    
    for i in range(n):
        while nums[i] < n and nums[i] != nums[nums[i]]:
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

    for i in range(n):
        if nums[i] != i:
            return i

    return n

print(find_missing_number([4, 0, 3, 1]))
