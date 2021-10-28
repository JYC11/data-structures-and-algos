import sys

N = int(sys.stdin.readline())
words = []
for _ in range(N):
    words.append(sys.stdin.readline().strip())
words = list(set(words))
words.sort()
words.sort(key=len)

for w in words:
    print(w)