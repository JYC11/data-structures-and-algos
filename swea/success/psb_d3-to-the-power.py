def to_the_power_of(base,power):
    if power == 1:
        return base
    else:
        answer = base * to_the_power_of(base, power-1)
    return answer

for test_case in range(1,11):
    t = int(input())
    base, power = list(map(int,input().split()))
    answer = to_the_power_of(base,power)
    print(f"#{test_case} {answer}")