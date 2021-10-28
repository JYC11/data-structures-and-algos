def longestPalindrome(s):
    di = {}
    for i in s:
        if i in di.keys():
            di[i] = di[i]+1
        else:
            di[i] = 1

    longest_pal_len = 0
    for k,v in di.items():
        longest_pal_len += v//2*2
        if longest_pal_len % 2 == 0 and v % 2 == 1:
            longest_pal_len += 1

    return longest_pal_len

longestPalindrome("bananas")