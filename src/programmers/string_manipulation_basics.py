import re


def solution(s):
    if len(s) == 4 or len(s) == 6:
        return "".join(re.findall("\d", s)) == s
    else:
        return False


print(solution("a234"))
