# import sys

# N = int(sys.stdin.readline())

# scores = list(map(int,sys.stdin.readline().split(" ")))

# maximum = max(scores)

# new_scores = [i/maximum*100 for i in scores]

# print(sum(new_scores)/N)

# import sys
# N = int(sys.stdin.readline())

# for _ in range(N):
#     n = bin(int(sys.stdin.readline()))[2:]
#     for idx, val in enumerate(n[::-1]):
#         if val == '1':
#             print(idx, end=' ')
