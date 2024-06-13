import sys
from collections import deque

N = int(sys.stdin.readline())

graph = []

for _ in range(N):
    row = list(map(int, sys.stdin.readline().strip().split()))
    row = [0 if r == 0 else "X" for r in row]
    graph.append(row)

print(graph)

"""
[0, 0][0, 1][0, 2]
[1, 0][1, 1][1, 2]
[2, 0][2, 1][2, 2]

positions = horizontal, vertical, diagonal

[x1,y1][x2,y2]
if y2 > y1 == horizontal
horizontal =
    [x1,y1] > [x1,y1+1], [x2,y2] > [x2,y2+1] => move right
    [x1,y1] > [x1,y1+1], [x2,y2] > [x2+1,y2+1] => move diagonal

if x2 > x1 == vertical
vertical = 
    [x1,y1] > [x1+1,y1], [x2,y2] > [x2+1,y2] => move down
    [x1,y1] > [x1+1,y1], [x2,y2] > [x2+1,y2+1] => move diagonal

if x2 > x1 && y2 > y1 == diagonal
diagonal = 
    [x1,y1] > [x1+1,y1+1], [x2,y2] > [x2,y2+1] => move right
    [x1,y1] > [x1+1,y1+1], [x2,y2] > [x2+1,y2] => move down
    [x1,y1] > [x1+1,y1+1], [x2,y2] > [x2+1,y2+1] => move diagonal

check for blank space, check for not visited, check for boundary

"""

hdx1 = [0, 0]
hdy1 = [1, 1]
hdx2 = [0, 1]
hdy2 = [1, 1]

vdx1 = [1, 1]
vdy1 = [0, 0]
vdx2 = [1, 1]
vdy2 = [0, 1]

ddx1 = [1, 1, 1]
ddy1 = [1, 1, 1]
ddx2 = [0, 1, 1]
ddy2 = [1, 0, 1]

# N = 6

# graph = [
#     [0,0,0,0,0,0],
#     [0,"X",0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0]
# ]

start = [[0, 0], [0, 1]]


def bfs(start):
    q = deque()
    q.append(start)

    while q:
        pipe_start, pipe_end = q.popleft()
        x1 = pipe_start[0]
        y1 = pipe_start[1]
        x2 = pipe_end[0]
        y2 = pipe_end[1]
        if x2 > x1 and y2 > y1:  # direction is diagonal
            for i in range(3):
                nx1 = x1 + ddx1[i]
                ny1 = y1 + ddy1[i]
                nx2 = x2 + ddx2[i]
                ny2 = y2 + ddy2[i]

                if i < 2:
                    if 0 <= nx1 < N and 0 <= ny1 < N and 0 <= nx2 < N and 0 <= ny2 < N:
                        if graph[nx1][ny1] != "X" and graph[nx2][ny2] != "X":
                            graph[nx2][ny2] = graph[x2][y2] + 1
                            q.append([[nx1, ny1], [nx2, ny2]])
                else:  # if moving diagonally
                    if (
                        0 <= nx1 < N
                        and 0 <= ny1 < N
                        and 0 <= nx2 < N
                        and 0 <= ny2 < N
                        and 0 <= nx1 + 1 < N
                        and 0 <= ny1 + 1 < N
                    ):
                        if (
                            graph[nx1][ny1] != "X"
                            and graph[nx2][ny2] != "X"
                            and graph[nx1 + 1][ny1] != "X"
                            and graph[nx1][ny1 + 1] != "X"
                        ):
                            graph[nx2][ny2] = graph[x2][y2] + 1
                            q.append([[nx1, ny1], [nx2, ny2]])

        elif y2 > y1:  # direction is horizontal
            for i in range(2):
                nx1 = x1 + hdx1[i]
                ny1 = y1 + hdy1[i]
                nx2 = x2 + hdx2[i]
                ny2 = y2 + hdy2[i]

                if i < 1:
                    if 0 <= nx1 < N and 0 <= ny1 < N and 0 <= nx2 < N and 0 <= ny2 < N:
                        if graph[nx1][ny1] != "X" and graph[nx2][ny2] != "X":
                            graph[nx2][ny2] = graph[x2][y2] + 1
                            q.append([[nx1, ny1], [nx2, ny2]])
                else:  # if moving diagonally
                    if (
                        0 <= nx1 < N
                        and 0 <= ny1 < N
                        and 0 <= nx2 < N
                        and 0 <= ny2 < N
                        and 0 <= nx1 + 1 < N
                        and 0 <= ny1 + 1 < N
                    ):
                        if (
                            graph[nx1][ny1] != "X"
                            and graph[nx2][ny2] != "X"
                            and graph[nx1 + 1][ny1] != "X"
                            and graph[nx1][ny1 + 1] != "X"
                        ):
                            graph[nx2][ny2] = graph[x2][y2] + 1
                            q.append([[nx1, ny1], [nx2, ny2]])

        elif x2 > x1:  # direction is vertical
            for i in range(2):
                nx1 = x1 + vdx1[i]
                ny1 = y1 + vdy1[i]
                nx2 = x2 + vdx2[i]
                ny2 = y2 + vdy2[i]

                if i < 1:
                    if 0 <= nx1 < N and 0 <= ny1 < N and 0 <= nx2 < N and 0 <= ny2 < N:
                        if graph[nx1][ny1] != "X" and graph[nx2][ny2] != "X":
                            graph[nx2][ny2] = graph[x2][y2] + 1
                            q.append([[nx1, ny1], [nx2, ny2]])
                else:  # if moving diagonally
                    if (
                        0 <= nx1 < N
                        and 0 <= ny1 < N
                        and 0 <= nx2 < N
                        and 0 <= ny2 < N
                        and 0 <= nx1 + 1 < N
                        and 0 <= ny1 + 1 < N
                    ):
                        if (
                            graph[nx1][ny1] != "X"
                            and graph[nx2][ny2] != "X"
                            and graph[nx1 + 1][ny1] != "X"
                            and graph[nx1][ny1 + 1] != "X"
                        ):
                            graph[nx2][ny2] = graph[x2][y2] + 1
                            q.append([[nx1, ny1], [nx2, ny2]])


bfs(start)
ans = graph[N - 1][N - 1] - 1
print(0 if ans < 0 else ans)
