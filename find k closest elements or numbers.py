'''
Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

Example 1:

Input: [5, 6, 7, 8, 9], K = 3, X = 7
Output: [6, 7, 8]
Example 2:

Input: [2, 4, 5, 6, 9], K = 3, X = 6
Output: [4, 5, 6]
Example 3:

Input: [2, 4, 5, 6, 9], K = 3, X = 10
Output: [5, 6, 9]
'''
from heapq import *

# Solution - 1


def find_closest_elements_1(arr, k, x):
    dict = []
    res = []

    for num in arr:
        tup = (num, abs(num-x))
        dict.append(tup)

    dict.sort(key=lambda x: x[1])

    for i in range(0, k):
        res.append(dict[i][0])

    return sorted(res)

# Solution - 2


def find_closest_elements_2(arr, k, x):
    min_heap = []

    for i in range(0, len(arr)):
        heappush(min_heap,  (abs(x-arr[i]), arr[i]))

    res = []

    for i in range(0, k):
        res.append(heappop(min_heap)[1])

    return sorted(res)


# Solution - 3

class Solution(object):

    def binary_search(self, arr, key):

        low = 0
        high = len(arr)-1

        while low <= high:

            mid = (low + high) // 2

            if key == arr[mid]:
                return mid

            if key > arr[mid]:
                low = mid + 1

            else:
                high = mid - 1

        if low > 0:
            return low - 1

        return low

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        index = self.binary_search(arr, x)

        low = index - k
        high = index + k

        low = max(low, 0)
        high = min(len(arr) - 1, high)

        min_heap = []

        for i in range(low, high+1):
            heappush(min_heap,  (abs(x-arr[i]), arr[i]))

        res = []

        for i in range(0, k):
            res.append(heappop(min_heap)[1])

        return sorted(res)
