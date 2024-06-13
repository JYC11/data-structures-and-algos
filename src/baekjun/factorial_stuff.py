import math
import sys

N = int(sys.stdin.readline())

fac = str(math.factorial(N))[::-1]

count = 0

for i in fac:
    if i == "0":
        count += 1
    else:
        break

print(count)
