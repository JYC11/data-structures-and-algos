from itertools import combinations

def solution(nums):
    combos = combinations(nums,3)
    answer = 0
    for i in combos:
        num = sum(i)
        if num > 1:
            for j in range(2,int(num/2)+1):
                if num%j == 0:
                    break
            else:
                answer += 1
    return answer
    

print(solution([1,2,7,6,4]))