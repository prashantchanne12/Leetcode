'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''

from collections import deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        sorted_order = []

        if numCourses <= 0:
            return True

        in_degrees = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}

        for parent, child in prerequisites:

            graph[parent].append(child)
            in_degrees[child] += 1

        sources = deque()

        for key in in_degrees:
            if in_degrees[key] == 0:
                sources.append(key)

        while sources:

            vertex = sources.popleft()
            sorted_order.append(vertex)

            for child in graph[vertex]:
                in_degrees[child] -= 1

                if in_degrees[child] == 0:
                    sources.append(child)

        if len(sorted_order) != numCourses:
            return False

        return True
