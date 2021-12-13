import sys
import math

input = sys.stdin.readline

A, B, V = map(int, input().split())

# A, B, V = [100,99,1000000000]

# A = climb, B = slide down, V = target height

ans = (V-B)/(A-B)

print(math.ceil(ans))

"""
((V-A)//(A-B))+1

2,1,5
day 1
0 + 2 - 1 = 1

day 2
1 + 2 - 1 = 2

day 3
2 + 2 - 1 = 3

day 4
3 + 2 = 5

(5 - 2)/(2 - 1) = 3
3 + 1


5,1,6
day 1
0 + 5 - 1 = 4

day 2 
4 + 5 = 9 

(6 - 5)/(5 - 1) = 1/4


3,2,7
day 1 
0 + 3 - 2 = 1

day 2
1 + 3 - 2 = 2

day 3
2 + 3 - 2 = 3

day 4
3 + 3 - 2 = 4

day 5
4 + 3 = 7

(7 - 3)/(3 - 2) = 4
4 + 1

100 99 1000000000
(1000000000 - 100)/(100-99) + 1

"""