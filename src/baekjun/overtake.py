import sys

N = int(sys.stdin.readline())

counter = 1

cars = set()
enter = {}
exit = []

for i in range(1, N + 1):
    carNum = sys.stdin.readline().strip()
    enter[carNum] = i

for _ in range(1, N + 1):
    carNum = sys.stdin.readline().strip()
    exit.append(carNum)

ans = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        if enter[exit[i]] > enter[exit[j]]:
            ans += 1
            break

print(ans)

"""
ZG206A,PU234Q,OS945CK,ZG431SN,ZG5962J enter
1      2        3       4       5


ZG5962J,OS945CK,ZG206A,PU234Q,ZG431SN exit

ZG5962J,OS945CK
5,3

OS945CK,ZG206A
5,1

ZG206A,PU234Q
1,2

PU234Q,ZG431SN
2,4

"""
