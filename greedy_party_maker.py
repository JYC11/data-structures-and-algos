adventurer_count = int(input())
adventurers = list[map(int, input().split(" "))]
adventurers.sort()

result = 0
count = 0

for i in adventurers:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)