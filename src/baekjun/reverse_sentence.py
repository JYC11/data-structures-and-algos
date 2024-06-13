import sys

N = int(sys.stdin.readline())

for _ in range(N):
    sentence = sys.stdin.readline().split()
    print(" ".join([word[::-1] for word in sentence]))
