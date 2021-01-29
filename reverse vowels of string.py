'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
'''


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        left = 0
        right = len(s) - 1
        v = 'aeiouAEIOU'
        str = [char for char in s]

        while left < right:
            if str[left] not in v:
                left += 1
            elif str[right] not in v:
                right -= 1
            elif str[left] in v and str[right] in v:
                temp = str[left]
                str[left] = str[right]
                str[right] = temp

                left += 1
                right -= 1

        return ''.join(str)
