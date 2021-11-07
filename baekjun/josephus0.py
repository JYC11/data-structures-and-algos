import sys
from collections import deque

N, M = list(map(int,sys.stdin.readline().split()))

queue = deque([i for i in range(1,N+1)])

result = []

while len(queue) > 0:
    queue.rotate(-M)
    popped = str(queue.pop())
    result.append(popped)

print('<'+', '.join(result)+'>')
