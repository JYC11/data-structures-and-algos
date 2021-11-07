import sys
import math

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

N = int(sys.stdin.readline())

nums = list(map(int,sys.stdin.readline().split()))

count = 0

for num in nums:
    if is_prime(num):
        count += 1

print(count)