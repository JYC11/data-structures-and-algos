import sys

N, M = list(sys.stdin.readline().split())

ans = 0

if len(str(N)) != len(str(M)):
    print(0)
else:
    if N[0] != M[0]:
        print(0)
    else:
        if N[0] == "8":
            ans += 1

        for i in range(1, len(N)):
            if N[i] != M[i]:
                break
            else:
                if N[i] == "8":
                    ans += 1
        print(ans)
