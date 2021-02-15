'''
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a < b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Example 1:

Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []

Example 3:

Input: firstList = [], secondList = [[4,8],[10,12]]
Output: []

Example 4:

Input: firstList = [[1,7]], secondList = [[3,10]]
Output: [[3,7]]
'''


class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """

        i = 0
        j = 0
        start = 0
        end = 1
        res = []

        while i < len(firstList) and j < len(secondList):

            a = firstList[i]
            b = secondList[j]

            # check if a overlaps b i.e. a's start time lies within b
            a_overlaps_b = a[start] >= b[start] and a[start] <= b[end]

            # check if b overlaps a i.e. b's start time lies within a
            b_overlaps_a = b[start] >= a[start] and b[start] <= a[end]

            if a_overlaps_b or b_overlaps_a:

                max_num = max(a[start], b[start])
                min_num = min(a[end], b[end])

                res.append([max_num, min_num])

            if a[end] < b[end]:
                i += 1
            else:
                j += 1

        return res
