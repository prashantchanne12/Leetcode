'''
Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.

You can assume that the array does not have any duplicates.

Example 1:

Input: [10, 15, 1, 3, 8]
Output: 2
Explanation: The array has been rotated 2 times.
'''


def count_rotations(arr):

    low = 0
    high = len(arr) - 1

    while low < high:

        mid = (low + high) // 2

        # if the mid is greater than the next element
        if mid < high and arr[mid] > arr[mid+1]:
            return mid + 1

        # if mid is smaller than he previous element
        if mid > low and arr[mid - 1] > arr[mid]:
            return mid

        # left is sorted, so pivot is on right side
        if arr[low] < arr[mid]:
            low = mid + 1

        # right is sorted, so pivot is on left side
        else:
            high = mid - 1

    return 0


print(count_rotations([10, 15, 1, 3, 8]))
print(count_rotations([1, 3, 8, 10]))
