from functools import reduce


def solution(left, right):
    answer = 0
    for n in range(left, right + 1):
        factors = set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
        if len(factors) % 2 == 0:
            answer += n
        else:
            answer -= n
    return answer


solution(13, 17)
