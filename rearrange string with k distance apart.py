'''
Given a string and a number ‘K’, find if the string can be rearranged such that the same characters are at least ‘K’ distance apart from each other.

Example 1:

Input: "mmpp", K=2
Output: "mpmp" or "pmpm"
Explanation: All same characters are 2 distance apart.
Example 2:

Input: "Programming", K=3
Output: "rgmPrgmiano" or "gmringmrPoa" or "gmrPagimnor" and a few more  
Explanation: All same characters are 3 distance apart.
Example 3:

Input: "aab", K=2
Output: "aba"
Explanation: All same characters are 2 distance apart.
Example 4:

Input: "aappa", K=3
Output: ""
Explanation: We cannot find an arrangement of the string where any two 'a' are 3 distance apart.
'''

from heapq import *
from collections import deque


def rearrange_string_with_k(string, k):

    if k <= 1:
        return string

    dict = {}

    for letter in string:
        if letter not in dict:
            dict[letter] = 0

        dict[letter] += 1

    max_heap = []
    # add all chars to max_heap
    for char, freq in dict.items():
        heappush(max_heap, (-freq, char))

    res = ''
    q = deque()

    print(max_heap)

    while max_heap:
        freq, char = heappop(max_heap)

        res += char

        # decrement freq and append to the queue
        q.append((char, freq+1))
        print(q)

        if len(q) == k:
            char, freq = q.popleft()

            if -freq > 0:
                heappush(max_heap, (freq, char))

    return res if len(res) == len(string) else ''


# if we were successful in appending all the characters to the result string,
# return it
print(rearrange_string_with_k('mmpp', 2))
# print(rearrange_string_with_k('aapa', 3))
