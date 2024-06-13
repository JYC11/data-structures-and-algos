import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    command = sys.stdin.readline().split()
    func = command[0]

    if func == "push":
        stack.append(command[1])
    elif func == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif func == "size":
        print(len(stack))
    elif func == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif func == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
