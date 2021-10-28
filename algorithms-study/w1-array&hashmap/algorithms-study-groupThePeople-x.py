from typing import *

class Solution: #hash map
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        
        for i in range(len(groupSizes)):
            if groupSizes[i] not in d.keys():
                d[groupSizes[i]] = [i]
            else:
                d[groupSizes[i]] += [i]

        result = []

        for k,v in d.items():
            for i in range(0,len(v),k):
                temp = v[i:i+k]
                result.append(temp)
        return result



s = Solution()
print(s.groupThePeople([2,1,3,3,3,2]))
print(s.groupThePeople([3,3,3,3,3,1,3]))

