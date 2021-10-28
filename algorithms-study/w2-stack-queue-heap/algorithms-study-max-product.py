from heapq import heappush, heapify, heappop

def maxProduct(nums): #heap
    heap = []
    heapify(heap)
    for i in nums:
        heappush(heap,-1*i)
    nums = []
    for i in range(2):
        nums.append(heappop(heap))
    return (nums[0]*-1-1)*(nums[1]*-1-1)


print(maxProduct([3,4,5,2]))