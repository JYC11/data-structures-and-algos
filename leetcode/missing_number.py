def missingNumber(nums):
    max_n = len(nums)
    nothing_missing = [i for i in range(0,max_n+1)]
    return list(set(nothing_missing) - set(nums))[0]

missingNumber([0])