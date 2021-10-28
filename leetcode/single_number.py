def singleNumber(nums):
    for i in set(nums):
        if nums.count(i) == 1:
            return i

singleNumber([4,1,2,1,2])