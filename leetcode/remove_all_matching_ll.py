class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyHead = currentHead = ListNode(0)
        while head != None:
            if head.val != val:
                currentHead.next = head
                currentHead = currentHead.next
            head = head.next
        currentHead.next = None
        return dummyHead.next