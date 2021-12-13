import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    jobs,location = map(int, sys.stdin.readline().split())
    priorities = map(int, sys.stdin.readline().split())

    queue = deque(priorities)
    answer = 0
    
    while True:
        popped = queue.popleft()
        location -= 1
        maximum = 0 if len(queue) == 0 else max(queue)
        if location != -1 and popped >= maximum:
            answer += 1
        elif location != -1 and popped < maximum:
            queue.append(popped)
        elif location == -1 and popped >= maximum:
            answer += 1
            break
        elif location == -1 and popped < maximum:
            queue.append(popped)
            location = len(queue)-1

    print(answer)