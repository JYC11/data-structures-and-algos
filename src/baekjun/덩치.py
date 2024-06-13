num_ppl = int(input())

ppl_list = []
ranks = []

for i in range(num_ppl):
    ppl_list.append(list(map(int, input().split(" "))))

for i in range(num_ppl):
    rank = 0
    for j in range(num_ppl):
        if ppl_list[i][0] < ppl_list[j][0] and ppl_list[i][1] < ppl_list[j][1]:
            rank += 1
    ranks.append(rank + 1)

for r in ranks:
    print(r, end=" ")
