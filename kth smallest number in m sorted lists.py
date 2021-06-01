'''
Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be verified from the merged 
list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7], K=3
Output: 7
Explanation: The 3rd smallest number among all the arrays is 7.
'''

from heapq import *

# Solution - 1


def find_kth_smallest(lists, k):

    min_heap = []

    for l in lists:
        for num in l:
            heappush(min_heap, num)

            if len(min_heap) > k:
                heappop(min_heap)

    return list(min_heap)[0]


print(find_kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5))
print(find_kth_smallest([[5, 8, 9], [1, 7]], 3))

# Solution - 2


def find_kth_smallest(lists, k):

    min_heap = []

    # put the 1st element of each list in the min_heap
    for i in range(len(lists)):
        heappush(min_heap, (lists[i][0], 0, lists[i]))

    number_count = 0
    number = 0

    while min_heap:

        number, i, l = heappop(min_heap)

        number_count += 1

        if number_count == k:
            break

        if len(l) > i+1:
            heappush(min_heap, (l[i+1], i+1, l))

    return number


print(find_kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5))
