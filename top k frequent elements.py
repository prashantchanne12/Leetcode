'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
'''


class Solution(object):
    def topKFrequent(self, nums, k):
        dict = {}
        list = []

        for num in nums:
            if num not in dict:
                dict[num] = 0

            dict[num] += 1

        dict = sorted(dict.items(), key=lambda x: x[1])
        print(dict)

        list = [x for x, y in dict[::-1]]

        return list[:k]


s = Solution()
print(s.topKFrequent([1, 3, 5, 12, 11, 12, 11], 2))

# Solution - 2

from heapq import *

def find_k_frequent_numbers(nums, k):
    
    dict = {}
    
    for num in nums:
        if num not in dict:
            dict[num] = 0
            
        dict[num] += 1

    min_heap = []
    
    for key, val in dict.items():
        heappush(min_heap, (val, key))
        
        if len(min_heap) > k:
            heappop(min_heap)
            
    res = []
    
    while min_heap:
        res.append(heappop(min_heap)[1])
        
    return res

    
print(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2))