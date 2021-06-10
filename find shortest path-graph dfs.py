graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def find_shortest_path_dfs(source, destination, visited, graph, dist):

    if source not in visited:

        visited.add(source)

        if source == destination:
            print(dist)

        for n in graph[source]:
            find_shortest_path_dfs(n, destination, visited, graph, dist+1)


visited = set()
print(find_shortest_path_dfs('A', 'E', visited, graph, 0))
