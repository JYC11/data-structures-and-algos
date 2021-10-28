def numIdenticalPairs(nums): #array
    num_dic = {}
    count = 0
    for i in range(len(nums)):
        num_dic[nums[i]] = num_dic.get(nums[i],0) + 1
    for i in num_dic:
        count += (num_dic[i]*(num_dic[i]-1))/2
    return int(count)