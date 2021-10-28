from typing import *

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        idx = arr.index(max(arr))
        right = True
        left = True
        while idx < len(arr)-1:
            if arr[idx] == arr[idx+1]:
                right = False
                break
            idx += 1
        
        while idx > 1:
            if arr[idx] == arr[idx-1]:
                left = False
                break
            idx -= 1

        if right and left:
            return arr.index(max(arr))

s = Solution()

print(s.peakIndexInMountainArray([3,4,5,1]))