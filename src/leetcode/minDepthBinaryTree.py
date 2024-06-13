from collections import deque

from src.leetcode import ListNode


class Solution:
    def minDepth(self, root: ListNode | None) -> int:
        if root is None:
            return 0
        q = deque()
        q.append(root)
        ans = 0
        while q:
            ans += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left is None and node.right is None:
                    return ans
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
