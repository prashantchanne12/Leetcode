'''
We are given an undirected graph that has characteristics of a k-ary tree. In such a graph, we can choose any node as the root to make a k-ary tree. The root (or the tree) with the minimum height will be called Minimum Height Tree (MHT). There can be multiple MHTs for a graph. In this problem, we need to find all those roots which give us MHTs. Write a method to find all MHTs of the given graph and return a list of their roots.

Example 1:

Input: vertices: 5, Edges: [[0, 1], [1, 2], [1, 3], [2, 4]]
Output:[1, 2]
Explanation: Choosing '1' or '2' as roots give us MHTs. In the below diagram, we can see that the 
height of the trees with roots '1' or '2' is three which is minimum.
'''

from collections import deque


def minimum_height_tree(nodes, edges):

    if nodes <= 0:
        return []

    # with only one node, since its in-degrees will be 0, therefore, we need to handle it seperately
    if nodes == 1:
        return [0]

    # 1) Initiialze the graph

    # count incoming edges
    in_degrees = {i: 0 for i in range(nodes)}

    # adjacency list graph
    graph = {i: [] for i in range(nodes)}

    # 2) Build the graph
    for parent, child in edges:

        # since this is an undirected graph, therefore, add a link for both nodes
        graph[parent].append(child)
        graph[child].append(parent)

        # increment the in_degrees of the both nodes
        in_degrees[parent] += 1
        in_degrees[child] += 1

    # 3) Find all leaves i.e. all nodes with 0 in-degrees
    leaves = deque()

    for key in in_degrees:
        if in_degrees[key] == 1:
            leaves.append(key)

    # 4) Remove leaves level by level and subtract each leave's children's in_degrees.
    # Repeat this until we ae left with 1 or 2 nodes, which will be our answer.
    # Any node that has already been a leaf cannot be the root of a minimum height tree, because it's adjacent non-leaf node will always be a better candidate
    total_nodes = nodes
    while total_nodes > 2:
        leaves_size = len(leaves)
        total_nodes -= leaves_size

        for i in range(0, leaves_size):
            node = leaves.popleft()

            # get the node's children to decrement their in-degrees
            for child in graph[node]:
                in_degrees[child] -= 1
                if in_degrees[child] == 1:
                    leaves.append(child)

    return list(leaves)


print(minimum_height_tree(5, [[0, 1], [1, 2], [1, 3], [2, 4]]))
print(minimum_height_tree(4, [[0, 1], [0, 2], [2, 3]]))
