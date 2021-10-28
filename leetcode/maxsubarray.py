import typing
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]


# def maxSubArray(nums):
#         if len(nums) == 1:
#             return nums[0]
#         elif len(nums) == 2:
#             if any(n < 0 for n in nums):
#                 return max(nums)
#             return nums[0] + nums[1]
#         elif all(n < 0 for n in nums):
#             return max(nums)
#         else:
#             left_max = 0
#             right_max = 0
#             max_num = max(nums)
#             index = nums.index(max_num,0)
#             left = index - 1
#             right = index + 1
            
#             while left >= 0:
#                 if index - 1 == left:
#                     left_tmp = max_num + nums[left]
#                 else:
#                     left_tmp = left_tmp + nums[left]
#                 if left_tmp > left_max:
#                     left_max = left_tmp
#                 left -= 1
            
#             while right < len(nums):
#                 if index + 1 == right:
#                     right_tmp = max_num + nums[right]
#                 else:
#                     right_tmp = right_tmp + nums[right]
#                 if right_tmp > right_max:
#                     right_max = right_tmp
#                 right += 1
            
#             current_max = max(left_max,right_max)
#             left = index - 1
#             right = index + 1
#             if left_max > right_max:
#                 while right < len(nums):
#                     if index + 1 == right:
#                         right_tmp = current_max + nums[right]
#                     else:
#                         right_tmp = right_tmp + nums[right]
#                     if right_tmp > current_max:
#                         current_max = right_tmp
#                     right += 1
#             else:
#                 while left >= 0:
#                     if index - 1 == left:
#                         left_tmp = current_max + nums[left]
#                     else:
#                         left_tmp = left_tmp + nums[left]
#                     if left_tmp > current_max:
#                         current_max = left_tmp
#                     left -= 1
            
#             return current_max