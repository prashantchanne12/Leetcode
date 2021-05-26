'''
How do we search in a sorted and rotated array that also has duplicates?

The code above will fail in the following example!

Example 1:

Input: [3, 7, 3, 3, 3], key = 7
Output: 1
Explanation: '7' is present in the array at index '1'.
'''


def search_in_rotated_array_with_duplicates(arr, key):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if key == arr[mid]:
            return mid

         # if the numbers at indices low, high, mid are same, we can't choose a side
         # the best we can do, is to skip one number from both end as key != arr[mid]

        if arr[low] == arr[mid] and arr[high] == arr[mid]:
            low += 1
            high -= 1

        # left sorted portion
        elif arr[low] <= arr[mid]:

            # check if key is present in left sorted portion
            # low to mid
            if key >= arr[low] and key < arr[mid]:
                high = mid - 1

            else:
                low = mid + 1

        else:
            # right sorted portion

            # check if key is present in the right sorted portion
            # mid to high

            if key <= arr[high] and key > arr[mid]:
                low = mid + 1
            else:

                high = mid - 1

    return -1


print(search_in_rotated_array_with_duplicates([3, 3, 7, 3, 3], 7))
