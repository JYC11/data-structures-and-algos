class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_ = ""

        for i in range(len(s)):
            if s[i] != "#":
                s_ += s[i]
            else:
                s_ = s_[:-1]

        t_ = ""

        for i in range(len(t)):
            if t[i] != "#":
                t_ += t[i]
            else:
                t_ = t_[:-1]

        return s_ == t_
