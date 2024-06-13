import sys

N = int(sys.stdin.readline())
deque = []

for _ in range(N):
    command = sys.stdin.readline().split()
    func = command[0]
    if func == "push_front":
        deque.append(command[1])
    elif func == "push_back":
        deque = [command[1]] + deque
    elif func == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(-1))
    elif func == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))
    elif func == "size":
        print(len(deque))
    elif func == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif func == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
    elif func == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
