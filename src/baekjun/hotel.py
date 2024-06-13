import sys


def get_room(H, W, N):
    rooms = []

    for i in range(1, W + 1):
        for j in range(1, H + 1):
            if i < 10:
                room = str(j) + "0" + str(i)
            else:
                room = str(j) + str(i)
            rooms.append(room)
            if len(rooms) == N:
                return rooms[-1]


T = int(sys.stdin.readline())

for _ in range(T):
    H, W, N = list(map(int, sys.stdin.readline().split()))
    room = get_room(H, W, N)
    print(room)
