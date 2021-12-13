import sys


for _ in range(4):
    x1,y1,x2,y2,x3,y3,x4,y4 = list(map(int,sys.stdin.readline().strip().split()))

    if x2 < x3 or y2 < y3 or x4 < x1 or y4 < y1:
        print("d")

    elif (x2 == x3 and y2 == y3) or (x2 == x3 and y1 == y4) or (x1 == x4 and y1 == y4) or (x1 == x4 and y2 == y3):
        print("c")
    
    elif y2 == y3 or x2 == x3 or y1 == y4 or x1 == x4:
        print("b")
    else:
        print("a")
