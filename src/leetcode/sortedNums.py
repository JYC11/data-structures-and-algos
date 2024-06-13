def sortedSquares(nums):
    nums = [i * i for i in nums]
    return sorted(nums)


print(sortedSquares([-7, -3, 2, 3, 11]))
