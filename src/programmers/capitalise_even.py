import re


def solution(s):
    answer = []
    s = s.split(" ")

    for i in range(len(s)):
        result = ""
        for j in range(len(s[i])):
            if j % 2 == 0:
                result += s[i][j].upper()
            else:
                result += s[i][j].lower()

        answer.append(result)

    return " ".join(answer)


def solution2(s):
    s = re.sub("\s{2,}", " ", s)
    words = s.split(" ")
    for i in range(len(words)):
        chars = [j for j in words[i]]
        for k in range(len(chars)):
            if k % 2 == 0:
                chars[k] = chars[k].upper()
            else:
                chars[k] = chars[k].lower()
        words[i] = "".join(chars)

    return " ".join(words)


print(solution("test one two three"))
