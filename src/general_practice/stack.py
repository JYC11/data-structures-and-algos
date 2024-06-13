from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


string = "We will conquere COVID-19"


def reverse_string(string):
    s = Stack()
    chars = [char for char in string]
    for char in chars:
        s.push(char)

    reversed = ""
    for i in range(len(chars)):
        char = s.pop()
        reversed = reversed + char

    return reversed


# couldn't figure this out
def is_match(ch1, ch2):
    match_dict = {")": "(", "]": "[", "}": "{"}
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch == "(" or ch == "{" or ch == "[":
            stack.push(ch)
        if ch == ")" or ch == "}" or ch == "]":
            if stack.size() == 0:
                return False
            if not is_match(ch, stack.pop()):
                return False

    return stack.size() == 0


print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
