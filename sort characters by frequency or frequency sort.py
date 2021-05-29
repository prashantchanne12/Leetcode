'''
Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

# Solution - 1


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {}
        res = ''

        for letter in s:
            if letter not in dict:
                dict[letter] = 0

            dict[letter] += 1

        dict = sorted(dict.items(), key=lambda x: x[1])

        for i in range(len(dict)-1, -1, -1):

            res += str(dict[i][0]) * dict[i][1]

        return res

# Solution - 2
