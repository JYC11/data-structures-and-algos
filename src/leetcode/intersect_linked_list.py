from src.leetcode import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode | None, headB: ListNode | None) -> ListNode | None:
        assert headA is not None
        assert headB is not None
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        if lenA > lenB:
            for i in range(lenA - lenB):
                assert headA is not None
                headA = headA.next
            while headA and headB:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next
        else:
            for i in range(lenB - lenA):
                assert headB is not None
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
