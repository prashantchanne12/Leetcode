from collections import deque


def is_scheduling_possible(vertices, edges):

    sorted_order = []

    if vertices <= 0:
        return sorted_order

    graph = {i: [] for i in range(vertices)}
    in_degrees = {i: 0 for i in range(vertices)}

    for parent, child in edges:

        graph[parent].append(child)

        in_degrees[child] += 1

    sources = deque()

    for key in in_degrees:
        if in_degrees[key] == 0:
            sources.append(key)

    while sources:

        node = sources.popleft()
        sorted_order.append(node)

        for child in graph[node]:

            in_degrees[child] -= 1

            if in_degrees[child] == 0:
                sources.append(child)

    if len(sorted_order) != vertices:
        return False

    return True


print(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]]))
