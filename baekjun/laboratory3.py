import sys
from collections import deque
from itertools import combinations
import copy

N,M = list(map(int, sys.stdin.readline().strip().split()))

graph = []
viruses = []

for i in range(N):
    row = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(N):
        if row[j] == 2:
            viruses.append((i,j))
            row[j] = "*"
        if row[j] == 1:
            row[j] = "-"

    graph.append(row)

print(graph)

dx = [1,-1,0,0]
dy = [0,0,1,-1]


comb = combinations(viruses,M)

def bfs(graph,visited,x,y):
    return

minimum_time = 1e10

for c in comb:
    for coords in c:
        temp = copy.deepcopy(graph)
        temp[coords[0]][coords[1]] = 1
        visited = [[False]*M for _ in range(N)]
        bfs(temp,visited,coords[0],coords[1])
    


