'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
'''


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        res = [[1]]

        for i in range(rowIndex):

            temp = [0] + res[-1] + [0]
            row = []

            for j in range(len(res[-1])+1):

                row.append(temp[j] + temp[j+1])

            res.append(row)

        return res[-1]
