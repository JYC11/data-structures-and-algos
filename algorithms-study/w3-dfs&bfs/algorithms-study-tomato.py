from collections import deque

M,N = list(map(int,input().split(" ")))

box = []

q = deque()

for i in range(N):
    box.append(list(map(int,input().split(" "))))
    for j in range(M):
        if box[i][j] == 1:
            q.append([i,j])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append([nx,ny])

bfs()

days = 0

for row in box:
    for tomato in row:
        if tomato == 0:
            print(-1)
            break
    days = max(max(row),days)

print(days-1)