'''
Share
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dict = {}
        current_length = 0
        max_length = 0
        current_sub_start = 0

        for i, letter in enumerate(s):
            if letter in dict and dict[letter] >= current_sub_start:
                current_sub_start = dict[letter]+1
                current_length = i - dict[letter]
                dict[letter] = i
            else:
                dict[letter] = i
                current_length += 1
                if current_length> max_length:
                    max_length = current_length

        return max_length

        