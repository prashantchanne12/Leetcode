'''
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
'''

class Solution(object):
    def findRelativeRanks(self, nums):
        dict = {}
        res = []
        index = 1
        for i in (sorted(nums)[::-1]):
            dict[i] = index
            index = index+1

        for i in nums:
            if dict[i] == 1:
                res.append('Gold Medal')
            elif dict[i] == 2:
                res.append('Silver Medal')
            elif dict[i] == 3:
                res.append('Bronze Medal')
            else:
                res.append(str(dict[i]))

        return res
        
        