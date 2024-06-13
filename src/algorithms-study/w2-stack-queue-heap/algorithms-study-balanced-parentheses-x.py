N = int(input())

arr = [input() for _ in range(N)]
# def check(string):
#     count = 0
#     for char in string:
#         if char == "(":
#             count += 1
#         elif char == ")":
#             count -= 1
#         if count < 0:
#             print("NO")
#             break
#     if count == 0:
#         print("YES")
#     elif count > 0:
#         print("NO")


def check(string):
    stack = []
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")


for i in arr:
    check(i)

"""
(())

(
[(]

(
[((]

)
popped = (
[(]
okay

)
popped = (
[]
okay

1,2,3,4,5,6,7



"""
