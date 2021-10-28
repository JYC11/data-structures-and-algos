from collections import Counter

A = int(input())
B = int(input())
C = int(input())

total = str(A*B*C)

counts = Counter(total)

for i in range(10):
    count = counts.get(str(i),0)
    print(count)
