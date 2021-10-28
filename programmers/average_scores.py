def solution(scores):
    answer = ''

    transposed = [list(i) for i in [*zip(*scores)]]

    for i in range(len(transposed)):
        row = transposed[i]
        maximum = max(row)
        max_cnt = len([i for i in row if i == maximum])
        minimum = min(row)
        min_cnt = len([i for i in row if i == minimum])
        self_score = transposed[i][i]
        if maximum == self_score and max_cnt == 1:
            transposed[i][i] = "@"
        if minimum == self_score and min_cnt == 1:
            transposed[i][i] = "@"
    
    transposed = [[j for j in i if j != "@"] for i in transposed]
    score_list = [sum(i)/len(i) for i in transposed]

    for score in score_list:
        if score >= 90:
            answer += 'A'
        elif score >= 80:
            answer += 'B'
        elif score >= 70:
            answer += 'C'
        elif score >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer

solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])