import sys

N, M = list(map(int, sys.stdin.readline().split()))

passwords = {}

for _ in range(N):
    website, pwd = sys.stdin.readline().strip().split()
    passwords[website] = pwd

for _ in range(M):
    toFind = sys.stdin.readline().strip()
    print(passwords[toFind])
