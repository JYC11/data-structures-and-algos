def solution(N, stages):
    ppl = len(stages)
    stuck_rates = {}

    for i in range(1, N + 1):
        if ppl != 0:
            stuck_count = stages.count(i)
            stuck_rates[i] = float(stuck_count) / float(ppl)
            ppl = ppl - stuck_count
        else:
            stuck_rates[i] = 0

    return [i[0] for i in sorted(stuck_rates.items(), key=lambda x: x[1], reverse=True)]


print(solution(4, [4, 4, 4, 4, 4]))
