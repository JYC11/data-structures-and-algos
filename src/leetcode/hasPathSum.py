from src.leetcode import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False
        return self.dfs(root, 0, targetSum)

    def dfs(self, root, base, targetSum) -> bool:
        if root.left is None and root.right is None:
            return base + root.val == targetSum
        if root.left:
            left = self.dfs(root.left, base + root.val, targetSum)
        else:
            left = False
        if root.right:
            right = self.dfs(root.right, base + root.val, targetSum)
        else:
            right = False
        return right or left
