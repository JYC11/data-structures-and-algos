import sys

N, M, C = list(map(int, sys.stdin.readline().split()))

graph = [[0] * (M) for _ in range((N))]

for _ in range(C):
    x, y = list(map(int, sys.stdin.readline().split()))
    graph[x - 1][y - 1] = 1

print(graph)
