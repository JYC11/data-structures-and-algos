def climbStairs(n):
    dic = {}
    dic[2], dic[1] = 2, 1
    for v in range(3, n + 1):
        dic[v] = dic[v - 1] + dic[v - 2]
    return dic[n]


climbStairs(10)
