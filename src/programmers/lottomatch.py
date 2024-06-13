# my solution
def solution(lottos, win_nums):
    answer = []

    ranks = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    min_count = len(list(set(lottos) & set(win_nums)))
    zero_count = lottos.count(0)

    answer.append(ranks[min_count + zero_count])
    answer.append(ranks[min_count])
    return answer
