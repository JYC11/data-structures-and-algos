import sys

N = int(sys.stdin.readline())
queue = []

for _ in range(N):
    command = sys.stdin.readline().split()
    func = command[0]
    if func == "push":
        queue.append(command[1])
    elif func == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif func == "size":
        print(len(queue))
    elif func == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif func == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif func == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
