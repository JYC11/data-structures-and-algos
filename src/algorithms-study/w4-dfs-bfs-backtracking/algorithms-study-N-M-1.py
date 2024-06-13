import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# N,M = 4,2

result = []

check = [False] * (N + 1)


def recur():
    if len(result) == M:
        print(" ".join(map(str, result)))
        return
    for i in range(1, N + 1):
        if check[i] is False:
            check[i] = True
            result.append(i)
            recur()
            check[i] = False
            result.pop()


recur()
