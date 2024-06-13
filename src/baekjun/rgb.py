import sys
from collections import deque

N = int(sys.stdin.readline())

# N = 5

graph = []

for _ in range(N):
    colors = sys.stdin.readline().strip()
    colors = [i for i in colors]
    graph.append(colors)

# graph = [
#     ["R","R","R","B","B"],
#     ["G","G","B","B","B"],
#     ["B","B","B","R","R"],
#     ["B","B","R","R","R"],
#     ["R","R","R","R","R"],
# ]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[False] * N for _ in range(N)]


def bfs(x, y, color):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == color and visited[nx][ny] is False:
                    q.append((nx, ny))
                    visited[nx][ny] = True


answer = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] is False:
            bfs(i, j, graph[i][j])
            answer += 1


for i in range(N):
    for j in range(N):
        if graph[i][j] == "B":
            graph[i][j] = "B"
        else:
            graph[i][j] = "R"

answer2 = 0
visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] is False:
            bfs(i, j, graph[i][j])
            answer2 += 1

print(answer, answer2)
