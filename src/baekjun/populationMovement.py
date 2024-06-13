from collections import deque

# N,L,R = list(map(int,sys.stdin.readline().split()))
N, L, R = 4, 10, 50
graph = [[10, 100, 20, 90], [80, 100, 60, 70], [70, 20, 30, 40], [50, 20, 100, 10]]

# for _ in range(N):
#     row = list(map(int,sys.stdin.readline().split()))
#     graph.append(row)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y, graph, opened):
    q = deque()
    opened[x][y] = True
    q.append((x, y))
    total = 0
    countries = []

    total += graph[x][y]
    countries.append((x, y))

    while q:
        x, y = q.popleft()
        pop = graph[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and opened[nx][ny] is False:
                npop = graph[nx][ny]
                if L <= (abs(npop - pop)) <= R:
                    q.append((nx, ny))
                    opened[nx][ny] = True
                    total += npop
                    countries.append((nx, ny))

    average = total // len(countries)

    for a, b in countries:
        graph[a][b] = average

    return True if len(countries) > 1 else False


answer = 0
while True:
    opened = [[False] * N for _ in range(N)]
    stop = True

    for i in range(N):
        for j in range(N):
            if not opened[i][j]:
                check = bfs(i, j, graph, opened)
                if check:
                    stop = False
    if stop:
        break
    else:
        answer += 1

print(answer)
