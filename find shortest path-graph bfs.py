graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def find_shortest_path(source, destination):

    if source == destination:
        return 0

    visited = []
    q = []
    dist = 0

    q.append(source)
    visited.append(source)

    while q:

        node = q.pop(0)
        dist += 1

        for n in graph[node]:

            if n not in visited:

                if n == destination:
                    return dist

                q.append(n)
                visited.append(n)

    return None


print(find_shortest_path('A', 'F'))
