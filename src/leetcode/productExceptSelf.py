class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        i = 0
        p = 1
        left = [0 for i in range(len(nums))]
        while i < len(nums):
            left[i] = p
            p *= nums[i]
            i += 1

        i = len(nums) - 1
        p = 1
        right = [0 for i in range(len(nums))]
        while i >= 0:
            right[i] = p
            p *= nums[i]
            i -= 1

        answer = []
        for i in range(len(left)):
            answer.append(left[i] * right[i])

        return answer
