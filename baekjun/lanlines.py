import sys

K,N = list(map(int,sys.stdin.readline().split()))
lanLines = [int(sys.stdin.readline()) for _ in range(K)]

# K,N = 4,11
# lanLines = [802,743,457,539]

start = 1
end = max(lanLines)

while start <= end:
    mid = (start+end)//2
    lines = 0
    for i in lanLines:
        if lines > N:
            mid = mid + 1
        else:
            mid = mid - 1

print(end)
    