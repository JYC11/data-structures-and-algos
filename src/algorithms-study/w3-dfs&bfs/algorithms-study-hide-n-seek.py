from collections import deque

N, K = list(map(int, input().split(" ")))
# N = 5
# K = 17

maximum = 100001

time = [0] * maximum


def bfs(start):
    q = deque()
    q.append(start)

    while q:
        loc = q.popleft()
        if loc == K:
            print(time[loc])
            return
        for next in [loc + 1, loc - 1, loc * 2]:
            if 0 <= next < maximum and time[next] == 0:
                time[next] = time[loc] + 1
                q.append(next)


bfs(N)
