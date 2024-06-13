def solution(price, money, count):
    total_needed = sum([price * i for i in range(1, count + 1)])
    if total_needed > money:
        return total_needed - money
    else:
        return 0


print(solution(3, 20, 4))
