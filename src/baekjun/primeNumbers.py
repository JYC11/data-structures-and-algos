import math
import sys


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


N, M = list(map(int, sys.stdin.readline().split()))

# N,M = 3,16

for i in range(N, M + 1):
    if is_prime(i):
        print(i)
