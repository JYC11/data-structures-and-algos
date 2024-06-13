from collections import deque

nodes, edges, start = list(map(int, input().split(" ")))

graph = [[0] * (nodes + 1) for _ in range(nodes + 1)]

for _ in range(edges):
    n1, n2 = map(int, input().split(" "))
    graph[n1][n2] = graph[n2][n1] = 1
# DFS
visited = [False] * (nodes + 1)


def dfs(graph, node, visited):
    if visited[node]:
        return
    visited[node] = True
    print(node, end=" ")
    neighbors = [i for i, x in enumerate(graph[node]) if x == 1]
    for n in neighbors:
        dfs(graph, n, visited)


dfs(graph, start, visited)

# BFS

visited = [False] * (nodes + 1)


def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        neighbors = [i for i, x in enumerate(graph[node]) if x == 1]
        print(node, end=" ")
        for n in neighbors:
            if not visited[n]:
                queue.append(n)
                visited[n] = True


print()
bfs(graph, start, visited)
