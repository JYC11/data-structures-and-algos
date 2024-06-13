import sys
from heapq import heappop, heappush

N = int(sys.stdin.readline())

heap = []

for _ in range(N):
    heappush(heap, int(sys.stdin.readline()))

for _ in range(N):
    print(heappop(heap))
