nodes = int(input())
edges = int(input())
start = 1

graph = [[0] * (nodes + 1) for _ in range(nodes + 1)]

for _ in range(edges):
    n1, n2 = map(int, input().split(" "))
    graph[n1][n2] = graph[n2][n1] = 1

visited = [False] * (nodes + 1)
count = []


def dfs(graph, node, count, visited):
    if visited[node]:
        return
    visited[node] = True
    count.append(node)
    neighbors = [i for i, x in enumerate(graph[node]) if x == 1]
    for n in neighbors:
        dfs(graph, n, count, visited)


dfs(graph, 1, count, visited)
print(len(count) - 1)
