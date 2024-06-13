from src.leetcode import ListNode


class Solution:
    def reverselist(self, head: ListNode | None) -> ListNode | None:
        prev = None

        while head is not None:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

        return prev
