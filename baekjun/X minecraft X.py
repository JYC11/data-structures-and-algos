import sys
n, m, b = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# n, m, b = 3, 4, 99
# table = [[0, 0, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 1]]

height = 0
ans = 1000000000000000000000000000000
for i in range(257):
    remove = 0
    add = 0
    for j in range(n):
        for k in range(m):
            if table[j][k] < i:
                add += (i - table[j][k])
            else:
                remove += (table[j][k] - i)
    inventory = remove + b
    if inventory < add:
        continue
    time = 2 * remove + add
    if time <= ans:
        ans = time
        height = i
print(ans, height)