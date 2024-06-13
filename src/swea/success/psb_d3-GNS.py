test_cases = int(input())
for i in range(test_cases):
    test_num, length = input().split()
    alien_nums = input().split()
    translate_from = {
        "ZRO": 0,
        "ONE": 1,
        "TWO": 2,
        "THR": 3,
        "FOR": 4,
        "FIV": 5,
        "SIX": 6,
        "SVN": 7,
        "EGT": 8,
        "NIN": 9,
    }
    translate_to = {0: "ZRO", 1: "ONE", 2: "TWO", 3: "THR", 4: "FOR", 5: "FIV", 6: "SIX", 7: "SVN", 8: "EGT", 9: "NIN"}
    sorted_nums = sorted([translate_from[i] for i in alien_nums])
    back_to_alien = [translate_to[i] for i in sorted_nums]
    final_string = " ".join(back_to_alien)
    print(f"{test_num} {final_string}")
