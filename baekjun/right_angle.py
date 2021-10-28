import sys

while True:
    nums = list(map(int,sys.stdin.readline().split()))
    if sum(nums) == 0:
        break
    else:
        nums.sort()
        if nums[0]*nums[0] + nums[1]*nums[1] == nums[2]*nums[2]:
            print("right")
        else:
            print("wrong")
