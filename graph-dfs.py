def dfs(vertex, graph, values, seen):

    values.append(vertex)
    seen[vertex] = True

    connections = graph[vertex]

    for i in range(0, len(connections)):
        connection = connections[i]

        if connection not in seen:
            dfs(connection, graph, values, seen)

    return values


graph = [[1, 3], [0], [3, 8], [0, 4, 5, 2], [3, 6], [3], [4, 7], [6], [2]]
print(dfs(0, graph, [], {}))

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

arr = []


def dfs(graph, visited, node):

    if node not in visited:
        visited.add(node)
        arr.append(node)
        for n in graph[node]:
            dfs(graph, visited, n)


visited = set()
print(dfs(graph, visited, 'A'))
print(arr)
