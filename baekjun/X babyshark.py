import sys
from collections import deque

N = int(sys.stdin.readline())

graph = []
shark_location = []
shark_size = 2

for _ in range(N):
    row = list(map(int, sys.stdin.readline().strip().split()))
    graph.append(row)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark_location = [i,j]
            graph[i][j] = 0