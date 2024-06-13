num = int(input())

i = 0
count = 0
while True:
    if "666" in str(i):
        count += 1
    if count == num:
        break
    i += 1
print(i)
