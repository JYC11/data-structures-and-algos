from collections import deque

size = int(input())

graph = [list(map(int, input().split(" "))) for _ in range(size)]

# size = 3

# graph = [
#     [2,2,1],
#     [2,2,2],
#     [1,2,-1]
# ]


visited = [[False] * size for _ in range(size)]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] is True

    while q:
        x, y = q.popleft()
        step_size = graph[x][y]
        if step_size == -1:
            print("HaruHaru")
            return
        next_steps = [(x + step_size, y), (x, y + step_size)]

        for s in next_steps:
            if 0 <= s[0] < size and 0 <= s[1] < size and visited[s[0]][s[1]] is False:
                q.append(s)
                visited[s[0]][s[1]] = True

    print("Hing")


bfs(0, 0)
