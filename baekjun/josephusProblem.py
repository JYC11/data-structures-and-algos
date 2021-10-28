from collections import deque

N,K = list(map(int,input().split(" ")))

nums = [i for i in range(1,N+1)]

# K -= 1
# index = K
# answer = []
# while len(nums) > 1:
#     answer.append(nums.pop(index))
#     index = (index+K)%len(nums)
# answer = answer + nums


def josephus(nums,K):
    nums = deque(nums)
    result = []
    while len(nums) > 0:
        nums.rotate(-K)
        popped = nums.pop()
        result.append(popped)
    return result

result = josephus(nums,K)
print(str(result).replace("[","<").replace("]",">"))


"""
1,2,3,4,5,6,7

1,2,4,5,6,7
3

1,2,4,5,7
3,6

1,4,5,7
3,6,2

1,4,5
3,6,2,7

1,4
3,6,2,7,5

4
3,6,2,7,5,1

3,6,2,7,5,1,4

"""