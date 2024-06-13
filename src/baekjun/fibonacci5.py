import sys


def fibonacci(x):
    nums = [0, 1]
    for i in range(2, x + 1):
        nums.append(nums[i - 1] + nums[i - 2])
    return nums[x]


N = int(sys.stdin.readline())

print(fibonacci(N))
