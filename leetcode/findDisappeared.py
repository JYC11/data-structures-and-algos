def findDisappearedNumbers(nums):
    not_disappeared = [i+1 for i in range(len(nums))]
    return list(set(not_disappeared) - set(nums))

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))