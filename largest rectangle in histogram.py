'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:

Input: heights = [2,4]
Output: 4
'''


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        stack = []

        for i, h in enumerate(heights):

            start = i

            while stack and stack[-1][1] > h:

                index, height = stack.pop()
                area = height * (i - index)
                max_area = max(max_area, area)
                start = index

            stack.append((start, h))

        for index, h in stack:

            max_area = max(max_area, h * (len(heights) - index))

        return max_area
