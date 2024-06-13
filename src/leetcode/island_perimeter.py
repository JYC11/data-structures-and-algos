from collections import deque


def islandPerimeter(grid):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[False] * len(grid[0]) for i in range(len(grid))]
    perimeter = 0

    def bfs(x, y, perimeter):
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                    perimeter += 1
                elif grid[nx][ny] == 0:
                    perimeter += 1

                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] == 1 and visited[nx][ny] is False:
                        q.append((nx, ny))
                        visited[nx][ny] = True
        return perimeter

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and visited[i][j] is False:
                perimeter = bfs(i, j, perimeter)
    return perimeter


islandPerimeter([[1, 0]])
