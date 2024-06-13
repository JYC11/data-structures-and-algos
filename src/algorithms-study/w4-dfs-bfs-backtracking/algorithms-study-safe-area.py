import sys
from collections import deque

N = int(sys.stdin.readline())

graph = []

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)
# N = 5
# graph = [[6, 8, 2, 6, 2], [3, 2, 3, 4, 6], [6, 7, 3, 3, 2], [7, 2, 5, 3, 6], [8, 9, 5, 2, 7]]

flattened = sum(graph, [])
minimum = min(flattened)
maximum = max(flattened)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, h):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] > h and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


maximum_safe_area = minimum

for flooded_height in range(minimum, maximum + 1):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > flooded_height and not visited[i][j]:
                bfs(i, j, flooded_height)
                count += 1
    if count > maximum_safe_area:
        maximum_safe_area = count

print(maximum_safe_area)
