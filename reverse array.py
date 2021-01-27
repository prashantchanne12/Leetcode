'''
GEEKFORGEEKS

Given an array (or string), the task is to reverse the array/string.
Examples : 
 

Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}
'''


def reverseArray(arr):
    left = 0
    right = len(arr)-1

    while left < right:

        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp

        left += 1
        right -= 1

    print(arr)


reverseArray([1, 2, 3, 4, 5])
