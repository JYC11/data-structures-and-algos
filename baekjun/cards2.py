import sys
from collections import deque

N = int(sys.stdin.readline())

q = deque()

for card in range(1,N+1):
    q.append(card)

while len(q) > 1:
    throw_away = q.popleft()
    to_bottom = q.popleft()
    q.append(to_bottom)

print(q.popleft())