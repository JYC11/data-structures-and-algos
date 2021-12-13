import sys

N,M = list(map(int,sys.stdin.readline().split()))

pokedex = {}
reverse_pokedex = {}

for i in range(1,N+1):
    pkmn = sys.stdin.readline().strip()
    pokedex[str(i)] = pkmn
    reverse_pokedex[pkmn] = str(i)

for _ in range(M):
    to_find = sys.stdin.readline().strip()

    if to_find.isnumeric():
        print(pokedex[to_find])
    else:
        print(reverse_pokedex[to_find])
