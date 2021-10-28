class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ord_target = ord(target)
        ord_letters = [ord(i) for i in letters]
        ord_letters.sort()
        return chr([i for i in ord_letters if i > ord_target][0])
    
    