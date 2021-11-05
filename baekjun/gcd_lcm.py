import sys
import math

N,M = list(map(int,sys.stdin.readline().split()))

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

print(math.gcd(N,M))
print(lcm(N,M))