class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        temp = head
        while temp:
            if temp.next and temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head