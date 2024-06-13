# import sys

# strokes = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# name1 = sys.stdin.readline()
# name2 = sys.stdin.readline()

# new_name = ''

# for i in range(len(name1)):
#     new_name += name1[i]
#     new_name += name2[i]

# print(new_name)


def printLoop(x: int) -> None:
    for i in range(1, x + 1):
        oddOrEven: str = "Even" if i % 2 == 0 else "Odd"
        print(i, oddOrEven)


printLoop(10)
