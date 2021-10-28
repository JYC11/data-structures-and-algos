def subarraySum(nums,k):
        curr_sum, res = 0, 0
        prefixSums = {0: 1}
        
        for n in nums:
            curr_sum += n
            diff = curr_sum - k
            res += prefixSums.get(diff, 0)
            prefixSums[curr_sum] = 1 + prefixSums.get(curr_sum, 0)
            
        return res

def solution(A):
        summed = 0 
        answer = 0
        sums_dict = {0: 1}
        
        for num in A:
            summed += num
            answer += sums_dict.get(summed, 0)
            if answer > 1000000000:
                return -1
            sums_dict[summed] = 1 + sums_dict.get(summed, 0)
            
        return answer


# print(subarraySum([1,-1,1,1,1,1],3))
# print(subarraySum([2,-2,3,0,4,-7],0))