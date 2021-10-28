T = int(input())

for i in range(T):
    k = int(input()) #층
    n = int(input()) #호
    people = [x for x in range(1,n+1)]
    for i in range(k):
        for j in range(1,n):
            people[j] += people[j-1]
    print(people[-1])


def test(k,n):
    people = [x for x in range(1,n+1)]
    for i in range(k):
        for j in range(1,n):
            people[j] += people[j-1]
    print(people[-1])

test(2,3)
"""
0: 1,2,3,4
1: 1,3,6,10
2: 1,4,10,20
3: 1,5,15,35
"""