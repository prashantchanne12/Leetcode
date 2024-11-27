from collections import deque


def is_scheduling_possible(vertices, edges):

    sorted_order = []

    if vertices <= 0:
        return sorted_order

    graph = {i: [] for i in range(vertices)}
    in_degrees = {i: 0 for i in range(vertices)}

    for parent, child in edges:

        graph[parent].append(child)

        in_degrees[child] += 1

    sources = deque()

    for key in in_degrees:
        if in_degrees[key] == 0:
            sources.append(key)

    while sources:

        node = sources.popleft()
        sorted_order.append(node)

        for child in graph[node]:

            in_degrees[child] -= 1

            if in_degrees[child] == 0:
                sources.append(child)

    if len(sorted_order) != vertices:
        return False

    return True


print(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]]))

# Solution - 2

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereq_dict = { i:[] for i in range(0, numCourses) }

        for course, prereq in prerequisites:
            prereq_dict[course].append(prereq)

        
        # A course has 3 possible states:
        # visited -> course has been added to output
        # visiting -> course not added to output, but added to cycle
        # unvisited -> course not added to output or cycle

        output = []
        visited = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False

            if course in visited:
                return True

            cycle.add(course)
            
            for pre in prereq_dict[course]:
                if not dfs(pre):
                    return False

            cycle.remove(course)
            visited.add(course)
            output.append(course)

            return True

        for i in range(0, numCourses):
            if not dfs(i):
                return []
            
        return output



        