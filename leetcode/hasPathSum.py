from typing import *
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.dfs(root,0,targetSum)

    def dfs(self, root, base, targetSum) -> bool:
        if root.left == None and root.right == None:
            return base + root.val == targetSum
        if root.left:
            left = self.dfs(root.left, base+root.val, targetSum)
        else:
            left = False
        if root.right:
            right = self.dfs(root.right, base+root.val, targetSum)
        else:
            right = False
        return right or left