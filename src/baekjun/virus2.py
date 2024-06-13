computers = 7  # int(input())
connections = 6  # int(input())

# graph = [[] for _ in range(computers+1)]
visited = [False] * (computers + 1)
# for i in range(connections):
#     a,b = list(map(int, input().split(" ")))
#     graph[a].append(b)
#     graph[b].append(a)
graph = [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
cnt = 0


def dfs(v):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if visited[i] is False:
            dfs(i)
            cnt += 1


dfs(1)
print(cnt)
