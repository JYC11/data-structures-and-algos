import sys

N = int(sys.stdin.readline())

# tests = ["(())())",
# "(((()())()",
# "(()())((()))",
# "((()()(()))(((())))()",
# "()()()()(()()())()",
# "(()((())()("]

for _ in range(N):
    parentheses = sys.stdin.readline()
    stack = []
    for p in parentheses:
        if p == "(":
            stack.append(p)
        elif p == ")":
            if len(stack) == 0:
                print("NO")
                break
            else:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    print("NO")
                    break
    else:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")