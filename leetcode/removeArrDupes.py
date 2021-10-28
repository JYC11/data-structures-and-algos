def removeDuplicates(nums):
    answer = ["_" for i in range(len(nums))]
    for i in range(len(nums)):
        if nums[i] in answer:
            answer[i] = float('inf')
        else:
            answer[i] = nums[i]
    answer = sorted(answer)
    for i in range(len(nums)):
        nums[i] = answer[i]
    nums = [i for i in nums if i < float('inf')]
    print(nums)
    return len(nums)

removeDuplicates([1,1,2])
