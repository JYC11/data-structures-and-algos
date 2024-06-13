def minTimeToType(word):
    current_loc = "a"
    dist = 0
    for i in word:
        new_loc = abs((ord(i) - ord(current_loc)))
        dist += min(new_loc, 26 - new_loc)
        current_loc = i
    return dist + len(word)


minTimeToType("bza")
