n = input()

split_up = [int(i) for i in n]

result = split_up[0]

for i in range(1, len(split_up)):
    num = split_up[i]
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
