import sys

N = int(sys.stdin.readline())


def solution(answers):
    prev = 0
    answers = [i for i in answers]
    score = 0
    for i in range(len(answers)):
        if i == 0:
            if answers[i] == "O":
                prev += 1
                score += prev
            else:
                score += prev
        else:
            if answers[i] == "O":
                prev += 1
                score += prev
            elif answers[i] == "X":
                prev = 0
                score += prev
    print(score)


for _ in range(N):
    answers = sys.stdin.readline()
    solution(answers)

# solution("OOXXOXXOOO")
# solution("OOXXOOXXOO")
# solution("OXOXOXOXOXOXOX")
# solution("OOOOOOOOOO")
# solution("OOOOXOOOOXOOOOX")
