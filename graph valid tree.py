'''
Given `n` nodes labeled from `0` to `n-1` and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

**Example 1:**

```
Input:n = 5, andedges = [[0,1], [0,2], [0,3], [1,4]]Output: true
```

**Example 2:**

```
Input:n = 5,andedges = [[0,1], [1,2], [2,3], [1,3], [1,4]]Output: false
```

**Note**: you can assume that no duplicate edges will appear in `edges`. Since all edges are undirected, `[0,1]` is the same as `[1,0]` and thus will not appear together in `edges`
'''

def validTree(n, edges):
    if not n:
        return True
        
        
    adj = { i: [] for i in range(n) }
    
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)
        
    visit = set()
    
    def dfs(node, prev):
        if node in visit:
            return False
            
        visit.add(node)
        for n in adj[node]:
            if n == prev:
                continue
            
            if not dfs(n, node):
                return False
                
        return True
        
    return dfs(0, -1) and n == len(visit)