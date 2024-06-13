def solution(d, budget):
    max_departments = 0
    d = sorted(d)
    for i in range(len(d)):
        if d[i] <= budget:
            max_departments += 1
            budget -= d[i]
        else:
            break
    return max_departments


print(solution([1, 3, 2, 5, 4], 9))
