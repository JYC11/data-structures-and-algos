
def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers,target,0,0)
    return answer


def dfs(numbers,target,idx,summed):
    global answer
    if idx == len(numbers) and summed == target:
        answer += 1
        return
    elif idx == len(numbers):
        return
    dfs(numbers,target,idx+1,summed+numbers[idx])
    dfs(numbers,target,idx+1,summed-numbers[idx])

print(solution([1,1,1,1,1],3))


"""

[1,1,1]


binary tree depth first search

             start
       +1               -1
   +1      -1       +1      -1
+1   -1  +1  -1   +1  -1   +1  -1




"""