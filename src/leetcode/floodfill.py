from collections import deque


def floodFill(image, sr, sc, newColor):
    visited = [[False] * len(image[0]) for i in range(len(image))]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    original_colour = image[sr][sc]

    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True
    while q:
        x, y = q.popleft()
        if image[x][y] == original_colour:
            image[x][y] = newColor
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(image) and 0 <= ny < len(image[0]):
                if image[nx][ny] == original_colour and visited[nx][ny] is False:
                    q.append((nx, ny))
                    visited[nx][ny] = True
    print(image)
    return image


floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
