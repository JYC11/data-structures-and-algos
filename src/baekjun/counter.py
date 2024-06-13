from collections import Counter

word = input()

counts = Counter(word.lower()).most_common()

if len(counts) > 1:
    if counts[0][1] == counts[1][1]:
        print("?")
    else:
        print(counts[0][0].upper())
else:
    print(counts[0][0].upper())
