def countBits(n):
    return [bin(i).replace("0b", "").count("1") for i in range(0, n + 1)]


countBits(5)
