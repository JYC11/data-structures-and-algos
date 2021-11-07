import sys

input = sys.stdin.readline

N, M = map(int, input().split())

result = []

check = [False] * (N+1)

def recur(num):
    if num == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1,N+1):
        if check[i] == False:
            check[i] = True
            result.append(i)
            recur(num+1)
            check[i] = False
            result.pop()

recur(0)