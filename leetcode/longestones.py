
def findMaxConsecutiveOnes(nums):
    nums = [str(i) for i in nums]
    num_string = ''.join(nums)
    ones = num_string.split("0")
    lengths = [len(i) for i in ones]
    return max(lengths)

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))