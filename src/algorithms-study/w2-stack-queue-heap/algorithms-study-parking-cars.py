# Not my solution
# from collections import deque
# n, m = map(int, input().split())
# park_fee =dict()
# park_spots = [(i+1) for i in range(n)]
# spots_used = list()
# car_weight = dict()
# queue = deque()
# car_location = dict()
# money = 0
# for i in range(n):
#     park_fee[i+1] = int(input())

# for j in range(m):
#     car_weight[j+1] = int(input())
#     car_location[j+1] = 0
# idx =1
# for a in range(2*m):
#     car = int(input())
#     if car > 0:
#         if len(spots_used) != n:
#             spots_used.append(min(park_spots))
#             car_location[car] = min(park_spots)
#             money += car_weight[car]*park_fee[min(park_spots)]
#             park_spots.remove(min(park_spots))
#         else:
#             queue.append(car)
#     else:
#         park_spots.append(car_location[-car])
#         spots_used.remove(car_location[-car])
#         car_location[-car] = 0
#         if queue:
#             a = queue.popleft()
#             spots_used.append(min(park_spots))
#             car_location[a] = min(park_spots)
#             money += car_weight[a] * park_fee[min(park_spots)]
#             park_spots.remove(min(park_spots))

# print(money)
