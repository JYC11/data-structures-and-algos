from typing import *
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def backtrack(start, comb):
            if len(comb) == k:
                answer.append(comb.copy())
                return
            
            for i in range(start, n+1):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()
        
        backtrack(1, [])

        return answer

s = Solution()
print(s.combine(5,3))

# def combination(arr):
#     if len(arr) == 0:
#         return [[]]

#     combos = []

#     for combo in combination(arr[1:]):
#         combos += [combo, combo + [arr[0]]]
    
#     return combos

# print(combination([1,2,3]))