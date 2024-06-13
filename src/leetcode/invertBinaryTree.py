from src.leetcode import TreeNode


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:

        if root is None:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.right = left
        root.left = right

        return root
