from src.leetcode import ListNode


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        string = ""

        while head is not None:
            string += str(head.val)
            head = head.next

        return string == string[::-1]
