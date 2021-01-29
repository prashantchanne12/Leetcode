'''
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0
'''


class Solution(object):
    def strStr(self, haystack, needle):

        if needle == '':
            return 0

        m = len(haystack)
        n = len(needle)

        if n > m:
            return -1

        for i in range(0, m-n+1):
            count = 0
            for j in range(0, n):
                if haystack[i+j] == needle[j]:
                    count += 1

            if count == n:
                return i

        return -1
