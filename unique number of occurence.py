'''
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
'''

# Solution 1
class Solution(object):
    def uniqueOccurrences(self, arr):
        dict1 = {}
        dict2 = {}

        for i in arr:
            if i in dict1:
                dict1[i] = dict1[i] + 1
            else:
                dict1[i] = 1

        for i in dict1.values():
            if i in dict2:
                return False
            else:
                dict2[i] = True


        return True

# Solution 2
class Solution(object):
    def uniqueOccurrences(self, arr):
        dict = {}

        for i in arr:
            if i in dict:
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1

        return len(dict.values()) == len(set(dict.values()))