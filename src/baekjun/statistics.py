import sys
from collections import Counter

nums = []

N = int(sys.stdin.readline())

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()


def mean(nums):
    return round(sum(nums) / len(nums))


def median(nums):
    return nums[len(nums) // 2]


def mode(nums):
    counts = Counter(nums).most_common(2)
    if len(nums) > 1:
        if counts[0][1] == counts[1][1]:
            return counts[1][0]
        else:
            return counts[0][0]
    else:
        return counts[0][0]


def get_range(nums):
    return max(nums) - min(nums)


print(mean(nums))
print(median(nums))
print(mode(nums))
print(get_range(nums))
