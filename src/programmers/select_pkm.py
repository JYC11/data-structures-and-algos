def solution(nums):
    max_pokemons = int(len(nums) / 2)
    unique_pokemons = list(set(nums))
    max_selectable = unique_pokemons[:max_pokemons]
    return len(max_selectable)


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
