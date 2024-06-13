def bracket_match1(text):
    stack = []
    answer = 0
    for b in text:
        if b == "(":
            stack.append("(")
        if b == ")":
            if len(stack) == 0:
                answer += 1
            if len(stack) >= 1:
                stack.pop()
    return answer + len(stack)


def bracket_match2(text):
    balance = 0
    answer = 0
    for b in text:
        if b == "(":
            balance += 1
        if b == ")":
            if balance == 0:
                answer += 1
            if balance > 0:
                balance -= 1
    return answer + balance
