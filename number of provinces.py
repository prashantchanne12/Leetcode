'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 
'''

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = {0}
        count = 0
        adj_list = [[] for i in range(len(isConnected) + 1)]
        done = set()

        for i in range(0, len(isConnected)):
            for j in range(0, len(isConnected[0])):
                if isConnected[i][j] == 1 and i != j and (i, j) not in done and (j, i) not in done:
                    adj_list[i+1].append(j+1)
                    adj_list[j+1].append(i+1)
                    done.add((i, j))
                    
        print(adj_list)

        def dfs(node):
            visited.add(node)

            for n in adj_list[node]:
                if n not in visited:
                    dfs(n)

        for i in range(0, len(isConnected)+1):
            if i not in visited:
                count += 1
                dfs(i)

        return count
        

            