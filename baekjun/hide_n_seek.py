# from collections import deque

# N, K = list(map(int, input().split(" ")))
# MAX = 1000001
# dist = [0]*MAX

# def bfs():
#     q = deque()
#     q.append(N)
#     while q:
#         current_loc = q.popleft()
#         if current_loc == K:
#             print(dist[current_loc])
#             break
#         for next_loc in (current_loc+1,current_loc-1,current_loc*2):
#             if 0 <= next_loc < MAX and next_loc not in dist:
#                 dist[next_loc] = dist[current_loc]+1
#                 q.append(next_loc)

# bfs()
        
from collections import deque

# N, K = list(map(int, input().split(" ")))
N, K = 5, 17
visited = set()

steps = 0

def bfs(location,visited,target):
    queue = deque(location)
    visited.append(location)
    global steps
    while queue:
        current_loc = queue.popleft()
        if current_loc == target:
            break
        neighbors = [current_loc+1,current_loc-1,current_loc*2]
        for i in neighbors:
            if i not in visited:
                steps += 1
                q.append(i)
                visited.append(i)

bfs(N,visited,K)
print(steps)