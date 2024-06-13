# hashmap
from functools import reduce
from itertools import chain, combinations


def mult(x, y):
    return x * y


def my_solution(clothes):
    clothes_dict = {}
    answer = 0
    for stuff in clothes:
        clothes_dict[stuff[1]] = clothes_dict.get(stuff[1], 0) + 1

    combos = []

    for i in range(1, len(clothes_dict.keys()) + 1):
        combo = list(map(list, list(combinations(clothes_dict.keys(), i))))
        combos.append(combo)

    combos = list((chain(*combos)))

    for combo in combos:
        combo = [clothes_dict[i] for i in combo]
        answer += reduce(mult, combo)

    return answer


def solution(clothes):
    clothes_dict = {}

    for stuff in clothes:
        clothes_dict[stuff[1]] = clothes_dict.get(stuff[1], 0) + 1

    answer = reduce(lambda x, y: x * (y + 1), clothes_dict.values(), 1) - 1

    return answer


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
