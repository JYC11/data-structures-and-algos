def removeElement(nums, val):
    answer = ["_" for i in range(len(nums))]
    j = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] == val:
            count += 1
        if nums[i] != val:
            answer[j] = nums[i]
            j += 1

    for i in range(len(answer)):
        nums[i] = answer[i]

    del nums[len(nums) - count :]

    return len(nums)


def betterVersion(nums, val):
    while True:
        try:
            nums.remove(val)
        except Exception:
            break
    len(nums)


print(removeElement([3, 2, 2, 3], 3))
