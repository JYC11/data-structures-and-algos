def findNumbers(nums):
    nums = [str(i) for i in nums]
    even_count = 0
    for num in nums:
        if len(num) % 2 == 0:
            even_count += 1
    return even_count
