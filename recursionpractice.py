def solution1(n):
    if n == 0:
        return 0
    else:
        return n + solution1(n-1)

def solution2(n,m):
    if n==1 or m == 1:
        return 1
    else:
        return solution2(n-1,m) + solution2(n,m-1)

def solution3(n,m):
    if n == 0:
        return 0
    elif m == 0 or n < 0:
        return 1
    else:
        return solution(n-m,m) + solution(n,m-1)

