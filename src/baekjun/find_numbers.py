import sys

N = int(sys.stdin.readline())
nums1 = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums2 = list(map(int, sys.stdin.readline().split()))

for n in nums2:
    if n in nums1:
        print(1)
    else:
        print(0)
