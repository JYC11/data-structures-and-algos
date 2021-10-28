def moveZeroes(nums):
    j = 0
    for i in range(len(nums)):
        num = nums[i]
        if num != 0:
            nums[j] , nums[i] = nums[i], nums[j]
            j += 1
    return

moveZeroes([0,1,0,3,12])