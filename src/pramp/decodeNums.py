def decodeVariations(S):
    if len(S) == 0:
        return 1
    if S[0] == "0":
        return 0

    c1, c2 = 0, 0

    if int(S[:2]) <= 26 and len(S) >= 2:
        S1 = S[1:]
        S2 = S[2:]
        c1 = decodeVariations(S1)
        c2 = decodeVariations(S2)
    else:
        S1 = S[1:]
        c1 = decodeVariations(S1)
    return c1 + c2
