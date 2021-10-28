from collections import deque
from collections import Counter
from functools import reduce

N = int(input())

buildings = []

for i in range(N):
    buildings.append(list(map(int,input())))

visited = [[0]*N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,cnt):
    q = deque()
    q.append((x,y))
    visited[x][y] = cnt

    while q:
        x,y = q.popleft()
        for i in range(4):
            x_, y_ = x + dx[i], y + dy[i]
            if 0<=x_<N and 0<=y_<N:
                if buildings[x_][y_] == 1 and visited[x_][y_] == 0:
                    q.append((x_,y_))
                    visited[x_][y_] = cnt

cnt = 0

for i in range(N):
    for j in range(N):
        if buildings[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            bfs(i,j,cnt)

print(cnt)

flattened = reduce(lambda x,y : x+y, visited)

non_zero = [i for i in flattened if i > 0]

answer = sorted(list(Counter(non_zero).values()))

print('\n'.join(map(str,answer)))