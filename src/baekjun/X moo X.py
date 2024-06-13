import sys

N = int(sys.stdin.readline())


def solution(N):
    if N == 0:
        return "moo"
    else:
        return solution(N - 1) + "m" + ((N + 2) * "o") + solution(N - 1)


moo_string = solution(N)

print(moo_string[N - 1])
