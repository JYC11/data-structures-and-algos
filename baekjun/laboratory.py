"""
0인 좌표가 모두 들어간 어레이 []
위 어레이에서 3개 무작위로 선택
벽 세우기(1로 바꾸기)
퍼져나가게 하기
안전영역 count

"""
import sys
import copy
from itertools import combinations
from collections import deque

N,M = list(map(int,sys.stdin.readline().split()))

# N,M = 4,6

lab = []

# lab = [
#     [0,0,0,0,0,0],
#     [1,0,0,0,0,2],
#     [1,1,1,0,0,2],
#     [0,0,0,0,0,2],
# ]

for _ in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    lab.append(row)

zeroes = []
viruses = []

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            zeroes.append([i,j])
        if lab[i][j] == 2:
            viruses.append([i,j])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(graph,visited,x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = 2
                q.append((nx,ny))

ans = 0
comb = combinations(zeroes,3)


for c in comb:
    visited = [[False]*M for _ in range(N)]
    temp = copy.deepcopy(lab)
    safe_count = 0

    for coords in c:
        temp[coords[0]][coords[1]] = 1

    for virus in viruses:
        bfs(temp,visited,virus[0],virus[1])
    
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                safe_count += 1

    ans = max(ans,safe_count)

print(ans)    

