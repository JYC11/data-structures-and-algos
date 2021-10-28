from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        q = deque()
        q.append(root)
        ans = 0
        while q:
            ans += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left == None and node.right == None:
                    return ans
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)

