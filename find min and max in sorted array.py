def min_in_sorted_array(nums):

    left = 0
    right = len(nums) - 1

    while left < right:

        mid = (left + right) // 2

        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1

    return nums[left]


def max_in_sorted_array(nums):

    left = 0
    right = len(nums) - 1

    while left < right:

        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            right = mid
        else:
            left = mid + 1

    return nums[left]


print(max_in_sorted_array([3, 4, 5, 1, 2]))
print(min_in_sorted_array([3, 4, 5, 1, 2]))
