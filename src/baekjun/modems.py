import sys

N, C = list(map(int, sys.stdin.readline().strip().split()))

houses = []

for _ in range(N):
    houses.append(int(sys.stdin.readline()))
# N,C=5,3
# houses = [1,2,8,4,9]
houses.sort()

low = 0
high = 1000000000
ans = 0

while low <= high:
    mid = (low + high) // 2
    prev = houses[0]
    count = 1

    for i in range(len(houses)):
        if houses[i] - prev >= mid:
            prev = houses[i]
            count += 1

    if count >= C:
        ans = max(ans, mid)
        low = mid + 1
    else:
        high = mid - 1

print(ans)


"""
1,2,4,8,9

"""
