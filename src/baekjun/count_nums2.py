import sys
from collections import Counter

N = int(sys.stdin.readline())
nums1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums2 = list(map(int, sys.stdin.readline().split()))

# nums1 = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
# nums2 = [10, 9, -5, 2, 3, 4, 5, -10]

nums_dict = Counter(nums1)

for num in nums2:
    res = str(nums_dict.get(num, 0))
    print(res, end=" ")
