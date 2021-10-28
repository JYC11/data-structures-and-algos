hexadecimal = input()
hexadecimal = [i for i in hexadecimal]
hex_dict = {
    "A":10,
    "B":11,
    "C":12,
    "D":13,
    "E":14,
    "F":15
}

hexadecimal = [hex_dict[i] if i in hex_dict.keys() else i for i in hexadecimal]
hexadecimal.reverse()
final = 0
for i in range(len(hexadecimal)):
    final += int(hexadecimal[i])*(16**i)

print(final)