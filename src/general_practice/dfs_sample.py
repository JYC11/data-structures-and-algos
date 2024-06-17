graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited = [False] * 9


# starts with going with smallest
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end="")
    for i in graph[v]:
        dfs(graph, i, visited)


def depth_first_search(graph, start):
    stack = [start]
    visited = set()
    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        yield vertex
        visited.add(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)
