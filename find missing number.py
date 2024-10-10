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

    # Place each number at its correct index if possible
    for i in range(n):
        # Keep swapping until nums[i] is either out of range or at the correct position
        while nums[i] < n and nums[i] != nums[nums[i]]:
            # Swap nums[i] with nums[nums[i]] to move the number to its correct position
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

    # After the above sorting process, find the first index where the number is incorrect
    for i in range(n):
        if nums[i] != i:
            return i  # This index is where the missing number should be

    return n  # If all numbers are in their correct place, return n as the missing number

print(find_missing_number([4, 0, 3, 1]))
