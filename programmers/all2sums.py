from itertools import combinations
def solution(numbers):
    return sorted(list(set([sum(i) for i in combinations(numbers, 2)])))


print(solution([5,2]))