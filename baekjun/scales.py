import sys

N = list(sys.stdin.readline().split())

if ''.join(N) == '12345678':
    print("ascending")
elif ''.join(N) == '87654321':
    print("descending")
else:
    print("mixed")