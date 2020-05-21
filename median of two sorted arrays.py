'''
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

# Solution O(a+b)

import numpy as np

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        final = []
        i = 0
        j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                final.append(nums1[i])
                i += 1
            else:
                final.append(nums2[j])
                j += 1
                
        while i < len(nums1):
            final.append(nums1[i])
            i += 1
            
        while j < len(nums2):
            final.append(nums2[j])
            j += 1
            
        return np.median(final)

# Solution O(n)

import numpy as np

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        final = []
        i = 0
        j = 0
        
        while i < len(nums1) or j < len(nums2):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    final.append(nums1[i])
                    i += 1
                else:
                    final.append(nums2[j])
                    j += 1
                
            elif i < len(nums1):
                final.append(nums1[i])
                i += 1
                  
            elif  j < len(nums2):
                final.append(nums2[j])
                j += 1
                
            
        return np.median(final)