from itertools import combinations
card_count, target = list(map(int, input().split(" ")))
cards = list(map(int, input().split(" ")))

closest = 0

for combos in combinations(cards, 3):
    summed = sum(combos)
    if closest < summed <= target:
        closest = summed

print(closest)