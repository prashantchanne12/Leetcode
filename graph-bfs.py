# Solution 1


def bfs(graph):
    queue = [0]
    values = []
    seen = {}

    while len(queue) != 0:
        vertex = queue.pop(0)
        values.append(vertex)
        seen[vertex] = True

        connections = graph[vertex]

        for i in range(0, len((connections))):
            connection = connections[i]

            if connection not in seen:
                queue.append(connection)

    return values


graph = [[1, 3], [0], [3, 8], [0, 4, 5, 2], [3, 6], [3], [4, 7], [6], [2]]
print(bfs(graph))

# Solution - 2

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def bfs(visited, graph, node):
    visited = []
    q = []

    visited.append(node)
    q.append(node)

    while q:
        node = q.pop(0)

        for n in graph[node]:

            if n not in visited:
                visited.append(n)
                q.append(n)

    return visited


print(bfs(visited, graph, 'A'))
