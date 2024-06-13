def solution(n):
    reversed_base3 = ""

    while True:
        reversed_base3 += str(int(n % 3))
        n = int(n / 3)
        if n == 0:
            break

    reversed_base3 = str(int(reversed_base3))[::-1]
    answer = 0
    for i in range(len(reversed_base3)):
        answer += int(reversed_base3[i]) * (3**i)
    return answer


print(solution(45))
