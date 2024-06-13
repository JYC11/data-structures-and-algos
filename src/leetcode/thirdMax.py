def thirdMax(nums):
    if len(set(nums)) < 3:
        return max(nums)
    return sorted(list(set(nums)))[-3]
