import sys

N,M = list(map(int,sys.stdin.readline().strip().split()))

trees = list(map(int,sys.stdin.readline().strip().split()))

# N,M = 4,7
# trees = [20, 15, 10, 17]

trees.sort()

low = 0
high = max(trees)

while low <= high:
    mid = (low + high)//2
    
    logs = 0

    for x in trees:
        if x >= mid:
            logs += (x-mid)

    if logs >= M:
        low = mid + 1
    else:
        high = mid - 1

print(high)