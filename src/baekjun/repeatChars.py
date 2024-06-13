import sys

N = int(sys.stdin.readline())

for _ in range(N):
    n, word = sys.stdin.readline().split()
    answer = [c * int(n) for c in word]
    print("".join(answer))
