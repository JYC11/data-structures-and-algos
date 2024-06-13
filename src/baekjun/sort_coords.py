import sys

N = int(sys.stdin.readline())

coords = []

for _ in range(N):
    coord = list(map(int, sys.stdin.readline().split()))
    coords.append(coord)

# coords = [
#     [3, 4],
#     [1, 1],
#     [1, -1],
#     [2, 2],
#     [3, 3]
# ]

coords.sort(key=lambda x: (x[0], x[1]))

for coord in coords:
    print(coord[0], coord[1])
