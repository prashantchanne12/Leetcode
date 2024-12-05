'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = 0
        leftMax = 0

        for char in s:
            if char == "(":
                leftMin += 1
                leftMax += 1
            elif char == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                # consider closing )
                leftMin -= 1

                # considering opening (
                leftMax += 1

            if leftMax < 0:
                return False

            if leftMin < 0: # s = (*)(
                leftMin = 0

        return leftMin == 0