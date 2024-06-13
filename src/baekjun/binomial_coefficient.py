import math
import sys

N, K = list(map(int, sys.stdin.readline().split()))


def binomial_coefficient(a, b):
    answer = math.factorial(a) / (math.factorial(b) * math.factorial(a - b))
    return int(answer)


print(binomial_coefficient(N, K))
