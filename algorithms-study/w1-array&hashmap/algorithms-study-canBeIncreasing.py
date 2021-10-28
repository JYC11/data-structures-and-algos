def canBeIncreasing(nums): #hash map
    for i in range(len(nums)):
        temp = nums.copy()
        del temp[i]
        if all(i < j for i,j in zip(temp,temp[1:])):
            return True
    return False

print(canBeIncreasing([1,2,10,5,7]))
print(canBeIncreasing([2,3,1,2]))
print(canBeIncreasing([1]))
