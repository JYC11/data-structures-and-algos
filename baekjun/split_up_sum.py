target = int(input())

nums = []

for n in range(1,target):
    if n + sum([int(i) for i in str(n)]) == target:
        nums.append(n)

if len(nums) > 0:
    print(min(nums))
else:
    print(0)