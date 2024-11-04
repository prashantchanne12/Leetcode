'''
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 
'''


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1]*(len(edges) + 1)

        # find parent for given node
        def find(n):
            p = parent[n]

            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]

            return p

        # return False if nodes have same parent
        def union(n1, n2):
            parent1 = find(n1)
            parent2 = find(n2)

            if parent1 == parent2:
                return False

            if rank[parent1] > rank[parent2]:
                # parent1 is gonna be the parent
                parent[parent2] = parent1
                rank[parent1] += 1
            else:
                # parent2 is gonna be the parent
                parent[parent1] = parent2
                rank[parent2] += 1

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        
