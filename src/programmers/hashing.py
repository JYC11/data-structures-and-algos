N = int(input())
word = input()

alphabet = "abcdefghijklmnopqrstuvwxyz"

summed = 0

for i in range(len(word)):
    char = word[i]
    idx = alphabet.index(char) + 1
    summed += idx * (31 ** (i))

print(summed % 1234567891)
