import sys
from heapq import heapify, heappop, heappush

n,m = list(map(int,sys.stdin.readline().split()))
nums = list(map(int,sys.stdin.readline().split()))

heap = []

for i in nums:
    heappush(heap, i)

combine_count = 0

while combine_count < m:
    x = heappop(heap)
    y = heappop(heap)
    summed = x + y
    heappush(heap, summed)
    heappush(heap, summed)
    combine_count += 1

print(sum(heap))

"""
1,2,3,4

1+2 = 3

3,3,3,4

3+3= 6

6,6,3,4



"""