class Solution:
    def rob(nums):
        rob1 = 0
        rob2 = 0

        #[rob1,rob2,n,n+1....]
        for n in nums:
            temp = max(rob2+n,rob1)
            rob1 = rob2
            rob2 = temp
        return rob2