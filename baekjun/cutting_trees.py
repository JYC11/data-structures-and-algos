import sys

treesCount,logsNeeded = list(map(int,sys.stdin.readline().split()))
treeHeights = list(map(int,sys.stdin.readline().split()))

# treesCount,logsNeeded = 5,20
# treeHeights = [4, 42, 40, 26, 46]

minimum = 1
maximum = max(treeHeights)


while minimum <= maximum:
    mid = (minimum + maximum)//2
    logs = 0

    for tree in treeHeights:
        if tree >= mid:
            logs += (tree-mid)

    if logs >= logsNeeded:
        minimum = mid + 1
    else:
        maximum = mid - 1

print(maximum)