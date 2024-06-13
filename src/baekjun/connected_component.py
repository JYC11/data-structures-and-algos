import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    node, target = list(map(int, sys.stdin.readline().split()))
    graph[node].append(target)
    graph[target].append(node)  # undirected graph so need to add both ways


visited = [False] * (N + 1)


def bfs(graph, start, visited):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        node = q.popleft()
        for next in graph[node]:
            if not visited[next]:
                q.append(next)
                visited[next] = True


count = 0

for i in range(1, N + 1):
    if not visited[i]:
        bfs(graph, i, visited)
        count += 1

print(count)
