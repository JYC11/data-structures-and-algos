class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        results = []
        open_count = 0
        close_count = 0
        for b in s:
            if b == "{" or b == "[" or b == "(":
                stack.append(b)
                open_count += 1
            if b == "}" or b == "]" or b == ")":
                close_count += 1
                if len(stack) == 0:
                    return False
                results.append(self.compare(b, stack.pop()))
        if open_count != close_count:
            return False
        return all(results)

    def compare(self, target: str, to_compare: str) -> bool:
        bracket_dict = {"}": "{", "]": "[", ")": "("}
        return bracket_dict[target] == to_compare
