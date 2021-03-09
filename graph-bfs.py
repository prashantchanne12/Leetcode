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
