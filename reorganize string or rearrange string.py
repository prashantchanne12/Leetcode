'''
Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

Example 1:

Input: "aappp"
Output: "papap"
Explanation: In "papap", none of the repeating characters come next to each other.
Example 2:

Input: "Programming"
Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
Explanation: None of the repeating characters come next to each other.
Example 3:

Input: "aapa"
Output: ""
Explanation: In all arrangements of "aapa", atleast two 'a' will come together e.g., "apaa", "paaa".
'''

from heapq import *


class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        dict = {}

        for letter in s:
            if letter not in dict:
                dict[letter] = 0

            dict[letter] += 1

        max_heap = []

        for k, v in dict.items():
            heappush(max_heap, (-v, k))

        prev = ''
        res = ''
        prev_char = None
        prev_val = 0

        while max_heap:
            (v, k) = heappop(max_heap)

            res += k
            prev = k
            v = v*-1

            if prev_char and -prev_val > 0:
                heappush(max_heap, ((prev_val, prev_char)))

            prev_char = k
            prev_val = (v-1)*-1

        if prev_char and -prev_val > 0:
            res += prev_char

        for i in range(0, len(res)):

            if i > 0 and res[i] == res[i-1]:
                return ''

        return res
