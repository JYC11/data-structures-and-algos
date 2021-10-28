#dfs used here to find all connected points

height, width = map(int, input().split(" "))

tray = []

for i in range(height):
    tray.append(list(map(int,input())))

result = 0

def dfs(x,y):
    if x <= -1 or x >= height or y <= -1 or y >= width:
        return False
    if tray[x][y] == 0: #not visited
        tray[x][y] = 1 #mark as visited
        dfs(x-1, y) #search surrounding grid cells
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

for i in range(height):
    for j in range(width):
        if dfs(i,j) == True:
            result += 1

print(result)

