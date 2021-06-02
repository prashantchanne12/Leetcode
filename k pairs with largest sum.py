'''
Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum where each pair consists of numbers from both the arrays.

Example 1:

Input: L1=[9, 8, 2], L2=[6, 3, 1], K=3
Output: [9, 3], [9, 6], [8, 6] 
Explanation: These 3 pairs have the largest sum. No other pair has a sum larger than any of these.
Example 2:

Input: L1=[5, 2, 1], L2=[2, -1], K=3
Output: [5, 2], [5, -1], [2, 2] 

'''

from heapq import *


# Solution - 1

def find_k_largest_pairs(nums1, nums2, k):

    min_heap = []

    for i in range(0, min(k, len(nums1))):

        for j in range(0, min(k, len(nums2))):

            print(min_heap)

            if len(min_heap) < k:
                heappush(min_heap, (nums1[i] + nums2[j], i, j))

            else:
                # if sum of the two numbers from the two arrays is smaller than the smallest(top) elememt of the heap,
                # we can break here. Since the arrays are sorted in descending order
                # we'll not be able to find a pair with a higher sum moving forward
                if nums1[i] + nums2[j] < min_heap[0][0]:
                    break
                else:
                    # we have pair with a larger sum, remove top and insert this pair in the heap
                    heappop(min_heap)
                    heappush(min_heap, (nums1[i]+nums2[j], i, j))

    res = []
    for (num, i, j) in min_heap:
        res.append([nums1[i], nums2[j]])

    return res


print(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3))


# Solution - 2


def find_k_largest_pairs(nums1, nums2, k):

    min_heap = []

    for i in range(0, min(k, len(nums1))):

        for j in range(0, min(k, len(nums2))):

            heappush(min_heap, (nums1[i] + nums2[j], i, j))

            if len(min_heap) > k:
                heappop(min_heap)

    res = []
    for (num, i, j) in min_heap:
        res.append([nums1[i], nums2[j]])

    return res


print(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3))
