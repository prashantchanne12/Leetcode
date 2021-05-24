'''
Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: s = "12345"
Output: ["12345"]
Example 4:

Input: s = "0"
Output: ["0"]
'''


class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        permutations = []
        permutations.append(s)

        for i in range(0, len(s)):

            # process only chars, skip digits
            if s[i].isalpha():

                for j in range(0, len(permutations)):

                    chars = list(permutations[j])

                    # swap cases, if upper then convert to lowr
                    # and vise, versa
                    chars[i] = chars[i].swapcase()

                    permutations.append(''.join(chars))

        return permutations
