from src.leetcode import ListNode


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        length = self.getLen(head)
        if length == 1:
            return head
        mid = length // 2 + 1
        count = 0
        while head is not None:
            if count == mid - 1:
                return head
            count += 1
            head = head.next

    def getLen(self, head) -> int:
        count = 0

        while head is not None:
            count += 1
            head = head.next

        return count
