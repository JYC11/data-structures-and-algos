class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        if lenA > lenB:
            for i in range(lenA-lenB):
                headA = headA.next
            while headA and headB:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next
        else:
            for i in range(lenB-lenA):
                headB = headB.next
            while headA and headB:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next
        return None
    
    def getLength(self, head: ListNode) -> int:
        count = 0
        while head.next:
            count += 1
            head = head.next
        return count
    