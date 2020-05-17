'''
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 

Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666. 
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
'''

# Solution 1
class Solution(object):
    def maximum69Number (self, num):
        list = [str(x) for x in str(num)]
        max_num = num

        for i in range(len(list)):
            if int(list[i]) == 9:
                list[i] = '6'
                max_num = max(int(''.join(list)), max_num)
                list[i] = '9'
            else:
                list[i] = '9'
                max_num = max(int(''.join(list)), max_num)
                list[i] = '6'


        return max_num
                
# Solution 2
class Solution(object):
    def maximum69Number (self, num):
        nums = list(str(num))

        for i in range(len(nums)):
            if nums[i] == '6':
                nums[i] = '9'
                break 
        return "".join(nums)