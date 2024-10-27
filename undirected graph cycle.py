def cycle(adj_list):
    visited = [False for i in range(0, len(adj_list))]
    
    def check_is_cylce(node):
        # BFS
        q = []
        q.append((node, -1))
        visited[node] = True
        
        while q:
            node, parent = q.pop(0)
            
            for n in adj_list[node]:
                if n == parent:
                    continue
                
                if visited[n]:
                    return True
                
                q.append((n, node))
                visited[n] = True
        
    
    for i in range(0, len(visited)):
        if not visited[i] and check_is_cylce(i):
            return True
            
    return False
    
adj_list = [[1, 4], [0, 2, 6], [1, 3], [2, 5], [5, 0], [3, 4], [1]]
print(cycle(adj_list))
    