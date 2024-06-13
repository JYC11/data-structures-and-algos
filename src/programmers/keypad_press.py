fixed_l = {
    1: "L",
    4: "L",
    7: "L",
}
fixed_r = {3: "R", 6: "R", 9: "R"}
row_coords = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 3, 8: 3, 9: 3, "*": 4, 0: 4, "#": 4}
col_coords = {1: 1, 2: 2, 3: 3, 4: 1, 5: 2, 6: 3, 7: 1, 8: 2, 9: 3, "*": 1, 0: 2, "#": 3}


def get_distance(target, current):
    return abs(row_coords[target] - row_coords[current]) + abs(col_coords[target] - col_coords[current])


def solution(numbers, hand):
    current_l = "*"
    current_r = "#"
    answer = ""
    for num in numbers:
        if num in fixed_l.keys():
            answer = answer + "L"
            current_l = num
        elif num in fixed_r.keys():
            answer = answer + "R"
            current_r = num
        elif num in [2, 5, 8, 0]:
            r_dist = get_distance(num, current_r)
            l_dist = get_distance(num, current_l)
            if r_dist < l_dist:
                answer = answer + "R"
                current_r = num
            elif r_dist > l_dist:
                answer = answer + "L"
                current_l = num
            elif r_dist == l_dist:
                answer = answer + hand[0].upper()
                if hand[0].upper() == "R":
                    current_r = num
                else:
                    current_l = num
    return answer
