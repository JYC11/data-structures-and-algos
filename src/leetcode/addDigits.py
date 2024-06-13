def addDigits(num):
    while len(str(num)) > 1:
        num = sum([int(i) for i in str(num)])
    return num


addDigits(38)
