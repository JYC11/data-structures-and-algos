import sys

N,M = list(map(int,sys.stdin.readline().strip().split()))

noSee = set()
noHear = set()

for _ in range(N):
    noSee.add(sys.stdin.readline().strip())

for _ in range(M):
    noHear.add(sys.stdin.readline().strip())

intersection = noSee.intersection(noHear)
intersection = list(intersection)
intersection.sort()

print(len(intersection))
for i in intersection:
    print(i)