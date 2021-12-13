import sys

S = set()

N = int(sys.stdin.readline())

for _ in range(N):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        elif temp[0] == "empty":
            S = set()
    else:
        command,number = temp
        number = int(number)

        if command == "add":
            S.add(number)
        elif command == "remove":
            S.discard(number)
        elif command == "check":
            print(1 if number in S else 0)
        elif command == "toggle":
            if number in S:
                S.discard(number)
            else:
                S.add(number)