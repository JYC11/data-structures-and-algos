import sys

N, K = list(map(int, sys.stdin.readline().split()))

k_count = N // K
remainder = round(N % K)


nums = [k_count for _ in range(K)]

i = 0

while remainder > 0:
    nums[i] += 1
    remainder -= 1
    i += 1

res = 1

for n in nums:
    res *= n

print(res)

"""
1,1,1,2,2,2,2,2

"""
