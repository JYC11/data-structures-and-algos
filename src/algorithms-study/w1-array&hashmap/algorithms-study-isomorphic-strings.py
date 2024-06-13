def isIsomorphic(s, t):  # hash map
    length = len(s)
    char_map = {}
    new_str = ""
    for i in range(length):
        if s[i] not in char_map.keys() and t[i] not in char_map.values():
            char_map[s[i]] = t[i]
    for i in range(length):
        new_str += char_map.get(s[i], "")
    return new_str == t


print(isIsomorphic("badc", "baba"))
"""
b = b
a = a
d = b > wrong
c = a > wrong

a = b
b = a
a = b
b = a


"""
