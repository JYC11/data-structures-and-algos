def sortArrayByParity(nums):
    if len(nums) == 1:
        return nums
    return [i for i in nums if i % 2 == 0] + [i for i in nums if i % 2 == 1]
