num_count = int(input())

nums = list(map(int, input().split(" ")))
nums = [0] + nums
target = int(input())


def countRanges(nums, target):
    if target in nums:
        print("0")
        return
    nums.append(target)
    nums.sort()

    target_idx = nums.index(target)
    smaller = nums[target_idx - 1]
    larger = nums[target_idx + 1]

    # target is biggest in range
    less_than_range = target - smaller - 1

    # target is smallest in range
    larger_than_range = larger - target - 1

    # target is in middle in range
    middle_range = larger_than_range * less_than_range

    print(larger_than_range + less_than_range + middle_range)


countRanges(nums, target)

"""
[4,7,13,24,30]
10
9,10
8,10
10,11
10,12

9,11
9,12
8,11
8,12

[4,7,14,24,30]
9,10
8,10
10,11
10,12
10,13

9,11
9,12
9,13
8,11
8,12
8,13




"""
