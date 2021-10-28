import sys
from collections import deque

N, M, V = list(map(int,sys.stdin.readline().split()))

graph = [[] for _ in range(0,N+1)]

for _ in range(M):
    node, dest = list(map(int,sys.stdin.readline().split()))
    graph[node].append(dest)

visited_dfs = [False]*(N+1)

def dfs(graph,node,visited):
    if visited[node]:
        return
    visited[node] = True
    print(node, end=" ")
    for next in graph[node]:
        dfs(graph,next,visited)
   

dfs(graph,V,visited_dfs)

visited_bfs = [False]*(N+1) 

def bfs(graph,node,visited):
    visited[node] = True
    queue = deque()
    queue.append(node)

    while queue:
        next = queue.popleft()
        print(next, end=" ")
        for n in graph[next]:
            if not visited[n]:
                queue.append(n)
                visited[n] = True


print()
bfs(graph,V,visited_bfs)