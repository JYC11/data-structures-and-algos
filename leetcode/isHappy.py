def isHappy(n):
    MAX = 10000
    i = 0
    while i < MAX:
        if n == 1:
            return True
            break
        n = sum([int(i)**2 for i in str(n)])
        i += 1
    return False
print(isHappy(19))
