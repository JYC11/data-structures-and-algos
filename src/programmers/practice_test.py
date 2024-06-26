def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer = []
    score1, score2, score3 = 0, 0, 0

    for i in range(len(answers)):
        if one[i % 5] == answers[i]:
            score1 += 1
        if two[i % 8] == answers[i]:
            score2 += 1
        if three[i % 10] == answers[i]:
            score3 += 1

    temp = [score1, score2, score3]

    for index, score in enumerate(temp):
        if score == max(temp):
            answer.append(index + 1)

    return answer
