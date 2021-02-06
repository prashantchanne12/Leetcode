'''
An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.
Examples : 

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5
Note: Order of elements is not important here.
'''


def re_arrange(nums):

    left = 0
    right = len(nums) - 1

    while left < right:

        if nums[right] < 0 and nums[left] >= 0:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1

        elif nums[left] < 0:
            left += 1

        elif nums[right] > 0:
            right -= 1

    print(nums)


re_arrange([-12, 11, -13, -5, 6, -7, 5, -3, -6])
