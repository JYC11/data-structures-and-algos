import re
def solution(numbers): #array
    nums = map(str,numbers)
    num = ''.join(sorted(nums,reverse=True,key=lambda s: s*3))
    if re.match("0{1,}",num):
        return "0"
    else:
        return num

print(solution([6,10,2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0,0,0,0]))