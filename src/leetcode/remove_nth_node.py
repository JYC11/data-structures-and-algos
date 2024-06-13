from src.leetcode import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        for i in range(n + 1):
            fast = fast.next  # type: ignore

        while fast is not None:
            slow = slow.next  # type: ignore
            fast = fast.next

        slow.next = slow.next.next  # type: ignore
        return dummy.next
