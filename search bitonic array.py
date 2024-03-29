'''
Given a Bitonic array, find if a given ‘key’ is present in it. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

Example 1:

Input: [1, 3, 8, 4, 3], key=4
Output: 3
Example 2:

Input: [3, 8, 3, 1], key=8
Output: 1
Example 3:

Input: [1, 3, 8, 12], key=12
Output: 3
Example 4:

Input: [10, 9, 8], key=10
Output: 0
'''

def search_bitonic(arr, key):
  
  low = 0
  high = len(arr) - 1

  while low <= high:

    mid = (low + high) // 2

    if key == arr[mid]:
      return mid

    if arr[mid] > arr[mid+1] and key > arr[mid]:
      high = mid-1
    else:
      low = mid+1

  return -1

print(search_bitonic([1, 3, 8, 12], 12))
print(search_bitonic([10, 9, 8], 10))
print(search_bitonic([1,3,8,12,4,2], 4))
