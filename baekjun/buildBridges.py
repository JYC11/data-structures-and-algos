import math
N = int(input())

points = [list(map(int,input().split(" "))) for _ in range(N)]

def build(n,m):
    bridge = math.factorial(m) // (math.factorial(n)*math.factorial(m-n))
    print(bridge)

for p in points:
    build(p[0],p[1])