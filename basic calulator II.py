'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
'''

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        stack = []
        current = 0
        operator = "+"

        all_operators = {"+", "-", "*", "/"}

        for i in range(0, len(s)):
            char = s[i] 
            
            if char.isdigit():
                current = current * 10 + int(char)

            if char in all_operators or i == len(s) - 1:
                if operator == "+":
                    stack.append(current)

                elif operator == "-":
                    stack.append(-current)

                elif operator == "*":
                    stack[-1] = stack[-1] * current
                    
                elif operator == "/":
                    stack[-1] = int(stack[-1] / current)


                current = 0
                operator = char

        return sum(stack)


                    
                    



