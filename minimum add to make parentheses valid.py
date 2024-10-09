'''
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

 
Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3
 
'''

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # stack = []
        # stack.append("z")

        # for char in s:
        #     if char == "(":
        #         stack.append("(")
        #     if char == ")":
        #         if stack[-1] == "(":
        #             stack.pop()
        #             continue
        #         else:
        #             stack.append(")")

        # return len(stack)-1

        stack = []
        count = 0 

        for char in s:
            if char == "(":
                stack.append("(")
            else:
                if stack:
                    stack.pop()
                else:
                    count += 1

        return len(stack) + count 