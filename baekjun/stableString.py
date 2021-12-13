"""

    빈 문자열은 안정적이다.
    S가 안정적이라면, {S}도 안정적인 문자열이다.
    S와 T가 안정적이라면, ST(두 문자열의 연결)도 안정적이다.

{}, {}{}, {{}{}}는 안정적인 문자열이지만, }{, {{}{, {}{는 안정적인 문자열이 아니다.

문자열에 행할 수 있는 연산은 여는 괄호를 닫는 괄호로 바꾸거나, 닫는 괄호를 여는 괄호로 바꾸는 것 2가지이다.

"""
import sys

counter = 1

def check(test_case):
    penalty = 0
    stack = []

    for char in test_case:
        if char == "{":
            stack.append(char)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                penalty += 1
                stack.append("}")

    return len(stack)//2+penalty


while True:
    test_case = sys.stdin.readline().strip()

    if "-" in test_case:
        break

    num = check(test_case)

    print(f"{counter}. {num}")

    counter += 1


"""
}{
{}{}{}
{{{}



}
balance = -1
}{
balance + 1 = 0

{}{}{}

{
left = 1
right = 0



"""