def addBinary(a, b):
    return bin(int(a, 2) + int(b, 2)).replace("0b", "")


addBinary("11", "1")
