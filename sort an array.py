'''
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
'''

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, left, mid, right):
            left_array = arr[left: mid + 1]
            right_array = arr[mid + 1: right + 1]

            i = left
            j = 0
            k = 0

            while j < len(left_array) and k < len(right_array):
                if left_array[j] <= right_array[k]:
                    arr[i] = left_array[j]
                    j += 1
                else:
                    arr[i] = right_array[k]
                    k += 1
                
                i += 1

            while j < len(left_array):
                arr[i] = left_array[j]
                j += 1
                i += 1

            while k < len(right_array):
                arr[i] = right_array[k]
                k += 1
                i += 1

            return arr

        def merge_sort(arr, left, right):
            # only one element left
            if left == right:
                return  arr

            mid = (left + right) // 2
            merge_sort(arr, left, mid) # left half
            merge_sort(arr, mid + 1, right) # right half
            merge(arr, left, mid, right)

            return arr


        return merge_sort(nums, 0, len(nums) - 1)