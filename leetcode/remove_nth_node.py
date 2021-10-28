class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        for i in range(n+1):
            fast = fast.next

        while fast != None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next