'''
Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

Given a directed graph, find the topological ordering of its vertices.

Example 1:

Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
Output: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0
'''

from collections import deque


def topological_sort(vertices, edges):

    sorted_order = []

    if vertices <= 0:
        return sorted_order

    # 1) initialize the graph

    # count of incoming edges
    in_degree = {i: 0 for i in range(vertices)}

    # adjacency list graph
    graph = {i: [] for i in range(vertices)}

    # 2) build the graph
    for parent, child in edges:
        # put the child into it's parent's list
        graph[parent].append(child)

        # increment the child's in_degree
        in_degree[child] += 1

    # 3) Find all sources i.e. all vertices with 0 in-degrees
    sources = deque()

    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    # 4) For each sources, add it to the sorted_order adn subtract one from all of its
    # children's in_degree
    # if a child's in_degree becomes zero, add it to the sources queue

    while sources:
        node = sources.popleft()
        sorted_order.append(node)

        for child in graph[node]:
            in_degree[child] -= 1

            if in_degree[child] == 0:
                sources.append(child)

    # topological sort is not possible as the graph has cycle
    if len(sorted_order) != vertices:
        return []

    return sorted_order


print(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))
