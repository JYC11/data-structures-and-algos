from src.leetcode import TreeNode


class Solution:
    def deleteDuplicates(self, head: TreeNode | None) -> TreeNode | None:
        if head is None:
            return head
        temp = head
        while temp:
            if temp.next and temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
