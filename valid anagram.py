'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

class Solution(object):
    def isAnagram(self, s, t):
        dict = {}
        
        if s == t:
            return True

        for i in s:
            if i in dict:
                dict[i] = dict[i] +1
            else:
                dict[i] = 1
        
        for i in t:
            if i in dict:
                dict[i] = dict[i]-1 
            else:
                return False
            
        return True if max(dict.values()) == 0 else False