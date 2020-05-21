'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
'''

class Solution(object):
    def wordPattern(self, pattern, str):
        dict = {}
        str = str.split(' ')
        
        if len(str) != len(pattern):
            return False

        for index, letter in enumerate(pattern):
            if letter in dict:
                if dict[letter] != str[index]:
                    return False
            else:
                if str[index] in dict.values():
                    return False
                dict[letter] = str[index]

        return True