from collections import deque

test_num = int(input())

# def dfs(x,y):
#     if x < 0 or x >= vertical or y < 0 or y >= horizontal:
#         return
#     if field[x][y] == 0:
#         return

#     field[x][y] = 0
#     dfs(x-1, y)
#     dfs(x, y-1)
#     dfs(x+1, y)
#     dfs(x, y+1)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    field[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < vertical and 0 <= ny < horizontal:
                if field[nx][ny] == 1:
                    field[nx][ny] = 0
                    q.append((nx, ny))


for i in range(test_num):
    horizontal, vertical, lettuces = list(map(int, input().split(" ")))
    field = [[0] * horizontal for _ in range(vertical)]
    count = 0

    for j in range(lettuces):
        x_, y_ = list(map(int, input().split(" ")))
        field[y_][x_] = 1

    for k in range(vertical):
        for x in range(horizontal):  # type ignore
            if field[k][x] == 1:
                bfs(k, x)
                count += 1

    print(count)
