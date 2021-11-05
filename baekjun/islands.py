import sys
from collections import deque

while True:
    dimensions = list(map(int,sys.stdin.readline().split()))
    
    if sum(dimensions) == 0:
        break
    else:
        w,h = dimensions
        graph = []

        for _ in range(h):
            graph.append(list(map(int,sys.stdin.readline().split())))

        dx = [1,-1,0,0,-1,1,1,-1]
        dy = [0,0,1,-1,-1,1,-1,1]

        # def dfs(x,y):
        #     if x < 0 or x >= h or y < 0 or y >= w:
        #         return False
        #     if graph[x][y] == 1:
        #         graph[x][y] = 0
        #         for i in range(8):
        #             nx = x + dx[i]
        #             ny = y + dy[i]
        #             dfs(nx,ny)
        #         return True
        #     return False

        def bfs(x,y):
            q = deque()
            q.append((x,y))

            while q:
                x,y = q.popleft()
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0<=nx<h and 0<=ny<w and graph[nx][ny] == 1:
                        graph[nx][ny] = 0
                        q.append((nx,ny))

        count = 0

        # for i in range(h):
        #     for j in range(w):
        #         if dfs(i,j):
        #             count += 1

        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    bfs(i,j)
                    count += 1

        print(count)

"""
0,0 0,1 0,2
1,0 1,1 1,2
2,0 2,1 2,2


"""