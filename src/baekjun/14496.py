import sys
from collections import deque

a, b = list(map(int, sys.stdin.readline().strip().split()))

N, M = list(map(int, sys.stdin.readline().strip().split()))

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = list(map(int, sys.stdin.readline().strip().split()))
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N + 1)


def bfs(start, graph, visited):
    q = deque()
    q.append((start, 0))
    visited[start] = True
    minimum_count = int(1e9)
    while q:
        node, dist = q.popleft()

        if node == b:
            minimum_count = min(minimum_count, dist)

        for i in graph[node]:
            if not visited[i]:
                q.append((i, dist + 1))
                visited[i] = True
    return minimum_count


minimum_count = bfs(a, graph, visited)

if minimum_count == int(1e9):
    print(-1)
else:
    print(minimum_count)
