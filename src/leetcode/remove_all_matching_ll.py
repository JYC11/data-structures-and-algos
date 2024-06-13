from src.leetcode import ListNode


class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummyHead = currentHead = ListNode(0)
        while head is not None:
            if head.val != val:
                currentHead.next = head
                currentHead = currentHead.next
            head = head.next
        currentHead.next = None
        return dummyHead.next
