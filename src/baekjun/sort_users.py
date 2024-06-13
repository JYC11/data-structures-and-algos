import sys

N = int(sys.stdin.readline())

# users = [[1,21,"Junkyu"],[2,21,"Dohyun"],[3,20,"Sunyoung"]]

users = []

for i in range(1, N + 1):
    temp = [i]
    user = list(sys.stdin.readline().split())
    user[0] = int(user[0])
    temp.extend(user)
    user.append(temp)

users.sort(key=lambda x: (x[1]))

for user in users:
    print(user[1], user[2])
