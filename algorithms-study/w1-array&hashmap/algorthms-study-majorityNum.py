from typing import *

class Solution: #hash map
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        di = {}
        
        for n in nums:
            if di.get(n,None) == None:
                di[n] = 1
            else:
                di[n] = di.get(n,None) + 1
        
        majority_count = 0
        for k,v in di.items():
            if v > majority_count:
                majority = k
                majority_count = v
        return majority
        

s = Solution()
print(s.majorityElement([3,3,4]))